import requests
from datetime import datetime, timedelta

_cached_base_date = None
_cached_response = None

def fetch_sun_info(lat: float, lng: float, base_date: str, next_date: str):
    global _cached_base_date, _cached_response
    
    if _cached_base_date == base_date:
        return _cached_response

    url = "https://api.sunrise-sunset.org/json"
    params = {
        'lat': lat,
        'lng': lng,
        'date': base_date,
        'formatted': 0
    }
    base_date_response = requests.get(url, params=params)
    base_date_data = base_date_response.json()
    base_date_results = base_date_data['results']

    url = "https://api.sunrise-sunset.org/json"
    params = {
        'lat': lat,
        'lng': lng,
        'date': next_date,
        'formatted': 0
    }
    next_date_response = requests.get(url, params=params)
    next_date_data = next_date_response.json()
    next_date_results = next_date_data['results']

    _cached_response = {
        'sunrise': datetime.fromisoformat(next_date_results['sunrise']).replace(tzinfo=None) + timedelta(hours=9),
        'sunset': datetime.fromisoformat(base_date_results['sunset']).replace(tzinfo=None) + timedelta(hours=9)
    }

    return _cached_response
