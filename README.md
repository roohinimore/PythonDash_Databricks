# Introduction 
Create a Python Dash application and get data from Azure Databricks DB. 

# Getting Started
**1. Databricks DB:**
- First create Azure Databricks Service in Azure Portal
- Launch Workspace and create Cluster in Databricks
- Insert Data from any CSV file or upload from samples provided by databricks, it will create table structures(under Data Science & Engineering tab).
- Start the Warehouse and get the connection details from it(we will need this to connect python-dash app to databricks db)

**2. Python Dash App:**
- Add databricks connection details and connect to specific database and table and write some sql queries.

# Build and Test
You may build and deploy application locally or using YAML CI/CD pipeline(.yml file is also provided in repo)
- py app.py OR python app.py

# Reference
https://docs.databricks.com/dev-tools/python-sql-connector.html

![image](https://user-images.githubusercontent.com/94110694/220609937-fc5c323f-573d-4838-85dc-58bd407858dd.png)
