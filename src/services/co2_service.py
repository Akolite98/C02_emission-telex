import requests
from src.config.env import CO2SIGNAL_API_URL, CO2SIGNAL_API_KEY

def fetch_co2_data(country_code):
    headers = {
        'auth-token': CO2SIGNAL_API_KEY
    }
    params = {
        'countryCode': country_code
    }
    try:
        response = requests.get(CO2SIGNAL_API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            'country': data.get('countryCode'),
            'carbon_intensity': data['data'].get('carbonIntensity'),
            'fossil_fuel_percentage': data['data'].get('fossilFuelPercentage'),
            'datetime': data['data'].get('datetime')
        }
    except requests.RequestException as e:
        print("Error fetching CO2 data:", e)
        return None
