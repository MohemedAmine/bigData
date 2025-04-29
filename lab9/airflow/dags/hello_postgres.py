from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 23),
    'catchup': False
}

with DAG(
    dag_id='hello_postgres',
    default_args=default_args,
    schedule_interval=None,
    tags=['postgres']
) as dag:

    drop_table = PostgresOperator(
        task_id='drop_testing_connection',
        postgres_conn_id='mypostgres_connection',
        sql="DROP TABLE IF EXISTS testing_connection;"
    )

    create_table = PostgresOperator(
        task_id='create_testing_connection',
        postgres_conn_id='mypostgres_connection',
        sql="""
            CREATE TABLE testing_connection (
                dummy_column INTEGER NOT NULL PRIMARY KEY
            );
        """
    )
    drop_table >> create_table