# File: tasks/fetch_weather_data.py

import requests
import json
import os
from datetime import datetime

def fetch_weather_data(**kwargs):
    # Load configuration
    config = kwargs['dag_run'].conf.get('weather_api_config', {})
    api_key = config.get('api_key', 'your_default_api_key')
    city = config.get('city', 'New York')
    
    # API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        
        # Create a simplified data structure
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Ensure the raw data directory exists
        os.makedirs('data/raw', exist_ok=True)
        
        # Save the data
        filename = f"data/raw/weather_data_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(weather_data, f)
        
        print(f"Weather data saved to {filename}")
        
        # Pass the filename to the next task
        return filename
    
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        raise