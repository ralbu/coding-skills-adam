import run_files

import logging
import requests
import re
import hashlib
from datetime import datetime


def get_item_path(item: dict[str, object], _path: str) -> str:
    return item["path"]


def is_dir(item: dict[str, object]) -> bool:
    return item["object_type"] == "DIRECTORY"


def is_file(item: dict[str, object]) -> bool:
    return item["object_type"] in ["NOTEBOOK", "LIBRARY"]


class NotebookRunner:
    def __init__(
        self,
        spark,
        dbutils,
        token: str,
        table_name: str,
        search_folder: str,
        excluded_files: str,
    ):
        self.spark = spark
        self.dbutils = dbutils

        self.workspace_url = (
            dbutils.notebook.entry_point.getDbutils()
            .notebook()
            .getContext()
            .apiUrl()
            .get()
            .replace("/api", "")
        )
        self.headers = {"Authorization": f"Bearer {token}"}

        self.table_name = table_name
        self.search_folder = search_folder

        self.excluded_files = re.split(r",\s*", excluded_files)
        self.excluded_files.append(
            dbutils.notebook.entry_point.getDbutils()
            .notebook()
            .getContext()
            .notebookPath()
            .get()
        )

    def create_table(self):
        self.spark.sql(f"""
        create table if not exists identifier('{self.table_name}') (
          id bigint generated always as identity,
          file_path string,
          inserted_at timestamp,
          file_hash binary
        )""")

    def get_items(self, path: str) -> list[dict[str, object]]:
        api_url = f"{self.workspace_url}/api/2.0/workspace/list"
        response = requests.get(api_url, headers=self.headers, params={"path": path})

        if response.status_code != 200:
            raise Exception(f"Failed to list files: {response.text}")

        items = response.json().get("objects", [])
        return items

    def get_file_contents(self, file_path) -> str:
        api_url = f"{self.workspace_url}/api/2.0/workspace/export"
        params = {"path": file_path, "format": "SOURCE"}
        response = requests.get(api_url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json().get("content")
        else:
            raise Exception(f"Failed to export notebook: {response.text}")

    def calculate_file_hash(self, file_path: str) -> bytearray:
        notebook_content = self.get_file_contents(file_path)
        return bytearray(hashlib.sha256(notebook_content.encode()).digest())

    def get_last_file_hash(self, file_path: str) -> bytearray | None:
        data = self.spark.sql(
            f"select file_hash from identifier('{self.table_name}') where file_path = '{file_path}' order by inserted_at desc"
        )
        first_row = data.first()
        return None if first_row is None else first_row[0]

    def get_notebooks(self) -> list[str]:
        return run_files.get_all_file_paths(
            self.search_folder,
            self.get_items,
            get_item_path,
            is_dir,
            is_file,
            self.excluded_files,
        )

    def has_ran(self, path: str) -> bool:
        data = self.spark.sql(
            f"select count(*) from identifier('{self.table_name}') where file_path = '{path}'"
        )
        return data.first()[0] > 0

    def has_changed(self, path: str) -> bool:
        calculated_hash = self.calculate_file_hash(path)
        last_hash = self.get_last_file_hash(path)
        return calculated_hash != last_hash

    def run_file(self, path):
        self.dbutils.notebook.run(path, 60)

    def file_ran(self, path):
        print(f"============ Ran file {path} ============")
        file_hash = self.calculate_file_hash(path)
        df = self.spark.createDataFrame(
            [[path, datetime.now(), file_hash]],
            ["file_path", "inserted_at", "file_hash"],
        )
        df.write.mode("append").saveAsTable("workspace.test.ran_files")

    def run(self):
        self.create_table()
        notebooks = self.get_notebooks()
        logging.info(f"Found notebooks: {notebooks}")

        run_files.run_files(
            notebooks, self.has_ran, self.has_changed, self.run_file, self.file_ran
        )
