# Databricks notebook source
# MAGIC %pip install --force-reinstall run_files-0.0.1-py3-none-any.whl
# MAGIC %restart_python

# COMMAND ----------

from run_files.databricks import NotebookRunner
import run_files

token = dbutils.secrets.get(scope = "files", key = "files")
table_name = dbutils.widgets.get("table_name")
search_folder = dbutils.widgets.get("search_folder")
excluded_files = dbutils.widgets.get("exclude")

notebook_runner = NotebookRunner(spark, dbutils, token, table_name, search_folder, excluded_files)

notebook_runner.run()