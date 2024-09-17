# File: tasks/clean_weather_data.py

import pandas as pd
import json
from datetime import datetime
import os

def clean_weather_data(**kwargs):
    ti = kwargs['ti']
    raw_data_file = ti.xcom_pull(task_ids='fetch_weather_data')
    
    if not raw_data_file:
        raise ValueError("No raw data file provided")
    
    # Read the raw JSON data
    with open(raw_data_file, 'r') as f:
        raw_data = json.load(f)
    
    # Convert to DataFrame
    df = pd.DataFrame([raw_data])
    
    # Perform cleaning operations
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['temperature'] = df['temperature'].round(1)
    df['humidity'] = df['humidity'].astype(int)
    
    # Ensure the processed data directory exists
    os.makedirs('data/processed', exist_ok=True)
    
    # Save the cleaned data
    output_file = f"data/processed/clean_weather_data_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(output_file, index=False)
    
    print(f"Cleaned weather data saved to {output_file}")
    
    return output_file