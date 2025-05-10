import requests
import pytz
from datetime import datetime


def fetch_sun_info(lat: float, lng: float, base_date: str, next_date: str):
    def convert_to_kst(utc_time_str):
        # UTC 시간 문자열을 datetime 객체로 변환 (naive datetime)
        utc_time = datetime.fromisoformat(utc_time_str.replace('Z', '+00:00'))  # Ensure it's in iso format
        # UTC 시간대 지정 (tzinfo가 설정되지 않았을 경우에만)
        if utc_time.tzinfo is None:
            utc_time = pytz.utc.localize(utc_time)  # time zone info를 추가
        # KST 시간대로 변환
        kst_time = utc_time.astimezone(pytz.timezone('Asia/Seoul'))
        return kst_time
    
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

    return {
        'sunrise': convert_to_kst(next_date_results['sunrise']),
        'sunset': convert_to_kst(base_date_results['sunset'])
    }
