from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook
import requests
import json
from datetime import datetime

def fetch_processor_details(**context):
    # Retrieve connection details
    connection = BaseHook.get_connection('mynifi_connection')
    schema = connection.schema or 'http'  # fallback to 'http' if empty
    host = connection.host
    port = connection.port

    # Build the NiFi API URL
    processor_id = '78b672d9-0196-1000-ffff-ffffb59c3de6'
    url = f'{schema}://{host}:{port}/nifi-api/processors/{processor_id}'

    # Send GET request
    response = requests.get(url)

    # Log the outputs
    print(f"Rest endpoint: {url}")
    print(f"Response: {response}")
    processor_details = response.json()
    print(f"Processor: {json.dumps(processor_details, indent=2)}")


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 23),
    'catchup': False
}

with DAG(
    dag_id='nifi_fetch_processor',
    default_args=default_args,
    schedule_interval=None,
    tags=['nifi']
) as dag:

    fetch_processor_task = PythonOperator(
        task_id='fetch_nifi_processor',
        python_callable=fetch_processor_details,
        provide_context=True,
    )

    fetch_processor_task