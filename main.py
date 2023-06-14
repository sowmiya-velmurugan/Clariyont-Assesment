import os
from dotenv import load_dotenv
from ml_component import ml_component
import requests
import json

load_dotenv()

csv_file_location = os.getenv('CSV_FILE_LOCATION')
target_column = os.getenv('TARGET_COLUMN')
api_url = os.getenv('API_URL')

tenant_data = {'name': 'Your Tenant Name'}
response = requests.post(f'{api_url}/tenant', json=tenant_data)
tenant = response.json()
print("Created Tenant:", tenant)

model_evaluation_results = ml_component(csv_file_location, target_column)
print("Model Evaluation Results:", model_evaluation_results)

project_metadata_data = {
    'tenant_id': tenant['id'],
    'csv_file_location': csv_file_location,
    'model_evaluation_results': model_evaluation_results
}
response = requests.post(f'{api_url}/project_metadata', json=project_metadata_data)
project_metadata = response.json()
print("Created Project Metadata:", project_metadata)

response = requests.get(f'{api_url}/tenant/{tenant["id"]}')
tenant = response.json()
print("Fetched Tenant:", tenant)

response = requests.get(f'{api_url}/project_metadata/{project_metadata["id"]}')
project_metadata = response.json()
print("Fetched Project Metadata:", project_metadata)
