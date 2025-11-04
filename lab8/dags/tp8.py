from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import json
import os
import requests

# Configuration par défaut du DAG
default_args = {
    'owner': 'john',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

# Télécharge les lancements à venir (en pur Python)
def download_launches():
    os.makedirs("/opt/airflow/dags/tmp", exist_ok=True)
    url = "https://ll.thespacedevs.com/2.0.0/launch/upcoming"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une erreur si la requête échoue
        with open("/opt/airflow/dags/tmp/launches.json", "w") as f:
            f.write(response.text)
    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement des lancements: {e}")
        raise

# Télécharge les images associées aux lancements
def get_pictures():
    os.makedirs("/opt/airflow/dags/tmp/images", exist_ok=True)
    
    try:
        with open("/opt/airflow/dags/tmp/launches.json") as f:
            launches = json.load(f)
    except Exception as e:
        print(f"Erreur de lecture du fichier JSON: {e}")
        raise

    for launch in launches.get("results", []):
        image_url = launch.get("image")
        if image_url:
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image_filename = image_url.split("/")[-1]
                image_path = f"/opt/airflow/dags/tmp/images/{image_filename}"
                with open(image_path, "wb") as f:
                    f.write(response.content)
            except requests.RequestException as e:
                print(f"Erreur lors du téléchargement de l'image: {e}")

# Définition du DAG
with DAG(
    dag_id='rocket_launches',
    default_args=default_args,
    description='Télécharge les images des prochains lancements de fusées',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='download_launches',
        python_callable=download_launches
    )

    task2 = PythonOperator(
        task_id='get_pictures',
        python_callable=get_pictures
    )

    task3 = BashOperator(
        task_id='notify',
        bash_command='echo "Nombre d\'images téléchargées: $(ls /opt/airflow/dags/tmp/images | wc -l)"'
    )

    # Orchestration des tâches
    task1 >> task2 >> task3
