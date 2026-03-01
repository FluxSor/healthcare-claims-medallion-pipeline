# Databricks notebook source
# MAGIC %md
# MAGIC ## Pipeline to ingest, clean and curate data

# COMMAND ----------

# Clear widgets (safe for interactive use; harmless in jobs)
dbutils.widgets.removeAll()

dbutils.widgets.text("reference_workspace_path", "[Your Databricks Profile]/healthcare-claims-medallion-pipeline/notebooks/")
notebook_path = dbutils.widgets.get("reference_workspace_path")
notebook_path

# COMMAND ----------

# This should only run once to create  Catalog and Schema Setup
dbutils.notebook.run(f"{notebook_path}01_catalog_schema_setup", 600)
# Run the healthcare claims bronze layer notebook
dbutils.notebook.run(f"{notebook_path}02_healthcare_claims_bronze", 600)
# Run the healthcare claims silver layer notebook
dbutils.notebook.run(f"{notebook_path}03_healthcare_claims_silver", 600)
# # # Run the healthcare claims gold layer notebook
dbutils.notebook.run(f"{notebook_path}04_healthcare_claims_gold", 600)