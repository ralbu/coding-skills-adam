# Databricks notebook source
spark.sql("""
create table if not exists workspace.test.ran_files (
  id bigint generated always as identity,
  file_path string,
  inserted_at timestamp,
  file_hash binary
)""")

# COMMAND ----------

import requests
import re

workspace_url = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get().replace("/api", "")
token = dbutils.secrets.get(scope = "files", key = "files")

def get_all_notebooks(path):
    notebooks = []
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{workspace_url}/api/2.0/workspace/list"
    response = requests.get(api_url, headers=headers, params={"path": path})
    if response.status_code == 200:
        objects = response.json().get("objects", [])
        for obj in objects:
            if obj["object_type"] == "DIRECTORY":
                notebooks.extend(get_all_notebooks(obj["path"]))
            elif obj["object_type"] in ["NOTEBOOK", "LIBRARY"]:
                notebooks.append(obj["path"])
    return notebooks


folder_path = dbutils.widgets.get("search_folder")
all_notebooks = get_all_notebooks(folder_path)

# Prevent recursively running this notebook
this_notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
if this_notebook_path in all_notebooks:
    all_notebooks.remove(this_notebook_path)

exclude_param = dbutils.widgets.get("exclude")
excludes = re.split(r',\s*', exclude_param)

if excludes != [""]:
    for exclude in excludes:
        if exclude not in all_notebooks:
            raise ValueError(f"Excluded notebook '{exclude}' not found in notebooks, from {all_notebooks}")
        all_notebooks.remove(exclude)

display(all_notebooks)

# COMMAND ----------

from datetime import datetime
import hashlib

def get_file_contents(file_path) -> str:
    headers = {"Authorization": f"Bearer {token}"}
    api_url = f"{workspace_url}/api/2.0/workspace/export"
    params = {
        "path": file_path,
        "format": "SOURCE"
    }
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("content")
    else:
        raise Exception(f"Failed to export notebook: {response.text}")

def calculate_file_hash(file_path: str) -> bytearray:
    notebook_content = get_file_contents(file_path)
    return bytearray(hashlib.sha256(notebook_content.encode()).digest())

def get_last_file_hash(file_path: str) -> bytearray|None:
    data = spark.sql(f"select file_hash from workspace.test.ran_files where file_path = '{file_path}' order by inserted_at desc")
    first_row = data.first()
    return None if first_row is None else first_row[0]

def log_run(file_path: str):
    file_hash = calculate_file_hash(file_path)
    # df = spark.createDataFrame(
    #     [[file_path, datetime.now()]], ["file_path", "sys_inserted_at"]
    # )
    df = spark.createDataFrame(
        [[file_path, datetime.now(), file_hash]], ["file_path", "inserted_at", "file_hash"]
    )
    df.write.mode("append").saveAsTable("workspace.test.ran_files")


def has_ran(file_path: str) -> bool:
    data = spark.sql(
        f"select count(*) from workspace.test.ran_files where file_path = '{file_path}'"
    )
    return data.first()[0] > 0

def has_changed(file_path: str) -> bool:
    calculated_hash = calculate_file_hash(file_path)
    last_hash = get_last_file_hash(file_path)
    return calculated_hash != last_hash

# COMMAND ----------

file_path = '/Users/albu.adam@gmail.com/.bundle/my_project/dev/files/src/new_folder/test_notebook'
file_hash = calculate_file_hash(file_path)
df = spark.createDataFrame(
    [[file_path, datetime.now(), file_hash]], ["file_path", "inserted_at", "file_hash"]
)
df.write.mode("append").saveAsTable("workspace.test.ran_files")

# COMMAND ----------

file_path = '/Users/albu.adam@gmail.com/.bundle/my_project/dev/files/src/new_folder/inner_folder/fail'
latest_notebook = spark.sql(f"select * from workspace.test.ran_files where file_path = '{file_path}' order by inserted_at desc limit 1")
display(latest_notebook)

file_hash = get_last_file_hash(file_path)
print("File hash", file_hash)
calculated_file_hash = calculate_file_hash(file_path)
print("Calculated hash", calculated_file_hash)

# COMMAND ----------

import logging

logging.basicConfig(level=logging.INFO, format="'%(asctime)s - %(levelname)s - %(message)s'")

total_notebooks = len(all_notebooks)
failed_notebooks = []
skipped_notebooks = []

for notebook_path in all_notebooks:
    if has_ran(notebook_path) and not has_changed(notebook_path):
        skipped_notebooks.append(notebook_path)
        logging.info(f"Skipped notebook (already ran and not changed): {notebook_path}")
        continue
    try:
        logging.info(f"Running notebook ({'has not ran/failed to run' if not has_ran(notebook_path) else 'has changed'}): {notebook_path}")
        dbutils.notebook.run(notebook_path, 60)
        log_run(notebook_path)
        logging.info(f"Finished running notebook: {notebook_path}")
    except Exception as e:
        logging.warning(f"Failed to run notebook: {notebook_path}, error: {e}")
        failed_notebooks.append(notebook_path)

if len(skipped_notebooks) == len(all_notebooks):
    logging.warning("All notebooks were skipped")
elif len(skipped_notebooks) > 0:
    logging.info(f"Skipped notebooks (already ran and not changed): {skipped_notebooks} ({len(skipped_notebooks)} of {total_notebooks})")
if len(failed_notebooks) > 0:
    text = f"Failed to run notebooks: {failed_notebooks} ({len(skipped_notebooks)} of {total_notebooks})"
    logging.warning(text)
    raise Exception(text)