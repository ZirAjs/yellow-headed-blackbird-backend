import requests
import random
from datetime import datetime

EBIRD_API_KEY = 'your_ebird_api_key'  # 환경변수로 처리해도 좋아요

def get_recent_birds_by_location(lat, lng, hours_back=3):
    url = f"https://api.ebird.org/v2/data/obs/geo/recent"
    headers = {"X-eBirdApiToken": EBIRD_API_KEY}
    params = {
        "lat": lat,
        "lng": lng,
        "back": 1,  # 1일 이내
        "maxResults": 100
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    # 시간 필터링: 최근 관찰된 시간 중 특정 시간대(예: 오전 6시~9시)에 해당하는 것만
    filtered = []
    for obs in data:
        if 'obsDt' in obs:
            try:
                obs_time = datetime.fromisoformat(obs['obsDt'])
                if 6 <= obs_time.hour <= 9:
                    filtered.append(obs)
            except:
                continue

    if not filtered:
        return None

    return random.choice(filtered)
