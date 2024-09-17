# Weather Data Pipeline

## Overview
This project fetches daily weather data from OpenWeatherMap and processes it using Apache Airflow. It's designed to demonstrate a simple ETL (Extract, Transform, Load) process.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- OpenWeatherMap API key

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weather_data_pipeline
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up Airflow:
   ```
   set AIRFLOW_HOME=%CD%
   airflow db init
   airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
   ```

6. Update API key:
   Edit `config/pipeline_config.yaml` and replace `your_openweathermap_api_key_here` with your actual OpenWeatherMap API key.

## Running the Pipeline

1. Start the Airflow webserver:
   ```
   airflow webserver --port 8080
   ```

2. In a new terminal window, start the Airflow scheduler:
   ```
   airflow scheduler
   ```

3. Open a web browser and go to `http://localhost:8080`

4. Log in with username `admin` and password `admin`

5. Find the `weather_data_pipeline` DAG and turn it on

The pipeline will now run daily, fetching and processing weather data.

## Project Structure
- `config/`: Configuration files
- `tasks/`: Python scripts for data fetching and processing
- `workflows/`: Airflow DAG definition
- `Dockerfile` and `docker-compose.yaml`: For Docker setup (optional)

## Troubleshooting
- If you encounter any "command not found" errors, make sure your virtual environment is activated.
- Check Airflow logs for detailed error messages if the pipeline fails.

## Next Steps
- Customize the pipeline for different cities or data points
- Add data visualization or reporting tasks
- Implement error handling and notifications

Enjoy your weather data pipeline!