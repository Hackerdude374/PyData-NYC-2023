# Weather Data Pipeline

## Overview
This project implements a daily weather data pipeline using Apache Airflow. It fetches weather data from OpenWeatherMap API, processes it, and stores both raw and cleaned data.

## Project Structure
```
weather_data_pipeline/
├── config/
│   └── pipeline_config.yaml
├── tasks/
│   ├── fetch_weather_data.py
│   └── clean_weather_data.py
├── workflows/
│   └── weather_pipeline.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Prerequisites
- Python 3.8+
- Docker (optional)
- OpenWeatherMap API key

## Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd weather_data_pipeline
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the API key
Edit `config/pipeline_config.yaml` and replace `your_openweathermap_api_key_here` with your actual API key.

### 5. Set up Airflow
```bash
export AIRFLOW_HOME=$(pwd)/airflow
airflow db init
airflow users create --username admin --firstname Your --lastname Name --role Admin --email your.email@example.com --password your_password
```

## Running the Pipeline

### Using Python and Airflow directly:

1. Start the Airflow webserver:
```bash
airflow webserver --port 8080
```

2. In a new terminal, start the Airflow scheduler:
```bash
airflow scheduler
```

3. Access the Airflow web interface at `http://localhost:8080` and enable the `weather_data_pipeline` DAG.

### Using Docker:

1. Build the Docker image:
```bash
docker build -t weather_pipeline .
```

2. Run the Airflow services:
```bash
docker-compose up -d
```

3. Access the Airflow web interface at `http://localhost:8080` and enable the `weather_data_pipeline` DAG.

## Customization
- To change the target city or other settings, edit `config/pipeline_config.yaml`.
- Modify the DAG schedule in `workflows/weather_pipeline.py` if you want to change the frequency of data collection.

## Troubleshooting
- If you encounter permission issues, ensure that the `data/raw` and `data/processed` directories exist and have write permissions.
- Check Airflow logs for detailed error messages if the pipeline fails.

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.