from datetime import time
import random

# 하드코딩된 Bird 리스트
birds = [
    {"name": "Sparrow", "time": time(14), "description": "A small bird"},
    {"name": "SSSSS", "time": time(14), "description": "A smrd"},
    {"name": "Eagle", "time": time(15), "description": "A large bird"},
    {"name": "Parrot", "time": time(16), "description": "A colorful bird"},
]

def get_daily_bird(input_time: time):
    minutes = input_time.minute
    if minutes < 30:
        target_time = time(input_time.hour, 0)
    else:
        target_time = time((input_time.hour + 1)%24, 0)

    active_birds = [bird for bird in birds if bird["time"] == target_time]
    
    # 해당 시간대에 맞는 bird 중 랜덤으로 하나 선택
    if active_birds:
        return random.choice(active_birds)
    else:
        return birds[0]