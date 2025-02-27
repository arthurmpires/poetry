# Databricks notebook source
# DBTITLE 1,Import libraries
import requests
import random
import json
import datetime

# COMMAND ----------

# DBTITLE 1,Get author data from API endpoint
url = 'https://poetrydb.org/'
author_endpoint = 'author'
response = requests.get(url+author_endpoint)

# COMMAND ----------

# DBTITLE 1,Save author data on the Unity Catalog
volume_path = '/Volumes/poetry/raw/poets'
file_name = 'authors'
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filepath = volume_path + '/' + file_name + '_' + timestamp + '.json'
with open(filepath, 'w') as file:
    json.dump(response.json(), file, indent=4)

# COMMAND ----------

# DBTITLE 1,Print the response of the API request
# print(response.json)

# COMMAND ----------

# DBTITLE 1,Describe the list of authors
# print(f'The database contains {len(response.json()["authors"]) } authors.')
# print()
# print('Some of them are:')
# random_authors = random.sample(response.json()['authors'], 5)
# for author in random_authors:
#     print(" - ", author)
