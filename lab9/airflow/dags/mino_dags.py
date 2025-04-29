from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.S3_hook import S3Hook
from datetime import datetime

# Function to upload file
def upload_file():
    file_path = '/tmp/test.txt'
    bucket_name = 'miniobucket'
    s3_key = 'test/testfile.txt'  # This will be the object name in the bucket

    # 1. Create and write to file
    with open(file_path, 'w') as f:
        f.write('Testfile contents.')
        f.flush()  # Ensure content is immediately written

    # 2. Upload file to MinIO using S3Hook
    s3_hook = S3Hook(aws_conn_id='myminio_connection')  # Define connection in Airflow UI
    s3_hook.load_file(
        filename=file_path,
        key=s3_key,
        bucket_name=bucket_name,
        replace=True
    )
    print(f"File {file_path} uploaded to bucket '{bucket_name}' with key '{s3_key}'.")

# Function to read file content
def read_file_content():
    bucket_name = 'miniobucket'
    s3_key = 'test/testfile.txt'

    # 1. Read file from MinIO using S3Hook
    s3_hook = S3Hook(aws_conn_id='myminio_connection')
    content = s3_hook.read_key(
        key=s3_key,
        bucket_name=bucket_name
    )

    # 2. Print file content
    print(f"Contents of {s3_key}:")
    print(content)

# DAG default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 28),
    'catchup': False
}

# Define the DAG
with DAG(
    dag_id='minio_file_upload_and_read',
    default_args=default_args,
    schedule_interval=None,
    tags=['minio', 's3']
) as dag:

    upload_file_task = PythonOperator(
        task_id='upload_file_task',
        python_callable=upload_file
    )

    read_file_content_task = PythonOperator(
        task_id='read_file_content_task',
        python_callable=read_file_content
    )

    # Define task sequence
    upload_file_task >> read_file_content_task
