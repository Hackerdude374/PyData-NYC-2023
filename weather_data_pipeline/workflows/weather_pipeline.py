# File: workflows/weather_pipeline.py

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add the tasks directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tasks'))

from fetch_weather_data import fetch_weather_data
from clean_weather_data import clean_weather_data

default_args = {
    'owner': 'weather_data_engineer',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A pipeline to fetch and clean weather data',
    schedule_interval=timedelta(days=1),
    catchup=False
)

fetch_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data,
    provide_context=True,
    dag=dag
)

clean_task = PythonOperator(
    task_id='clean_weather_data',
    python_callable=clean_weather_data,
    provide_context=True,
    dag=dag
)

fetch_task >> clean_task