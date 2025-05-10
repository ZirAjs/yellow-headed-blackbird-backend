from datetime import datetime, time

# 하드코딩된 Bird 리스트
birds = [
    {"name": "Sparrow", "time": time(14, 15), "description": "A small bird"},
    {"name": "Eagle", "time": time(15, 0), "description": "A large bird"},
    {"name": "Parrot", "time": time(16, 30), "description": "A colorful bird"},
]

def get_daily_bird(input_time: time):
    daily_bird = birds[0]

    # 하드코딩된 bird 리스트에서 가장 가까운 시간 찾기
    # for bird in birds:
    #     # Bird의 time을 datetime 객체로 변환하여 비교
    #     bird_time = datetime.combine(datetime.today(), bird["time"])  # 현재 날짜에 Bird의 시간 결합
    #     input_time_combined = datetime.combine(datetime.today(), input_time)  # 입력된 time을 현재 날짜와 결합
    
    return daily_bird
