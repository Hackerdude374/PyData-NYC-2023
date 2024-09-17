# File: Dockerfile

FROM apache/airflow:2.5.1

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Copy requirements file
COPY requirements.txt /requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Copy DAGs
COPY workflows/ ${AIRFLOW_HOME}/dags/
COPY tasks/ ${AIRFLOW_HOME}/dags/tasks/
COPY config/ ${AIRFLOW_HOME}/config/