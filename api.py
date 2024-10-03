
import requests
import json

def fetch_weather_data(city_name):
    api_key = "YOUR API KEY"  
    url = f'url={api_key}&q={city_name}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  
        return data
    else:
        return None
    
