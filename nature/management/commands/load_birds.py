from django.core.management.base import BaseCommand
from nature.models import Bird
from datetime import time

class Command(BaseCommand):
    help = 'Load hardcoded bird data'

    def handle(self, *args, **kwargs):
        Bird.objects.all().delete()
        from datetime import time

        birds = [
            {"name": "헛간올빼미", "time": time(0), "description": "헉산올빼미가 깨어있는 당신을 보고 놀랐습니다"},
            {"name": "수리부엉이", "time": time(0), "description": "수리부엉이가 당신의 열정에 힘입어 큰수리부엉이가 되었습니다"},
            {"name": "올빼미", "time": time(0), "description": "올빼미가 당신과 함께했습니다"},
            {"name": "검은관해오라기", "time": time(0), "description": "검은관해오라기가 당신에게 수고했다고 합니다"},
            {"name": "나이팅게일", "time": time(0), "description": "나이팅게일도 당신을 칭찬합니다"},

            {"name": "유럽쏙독새", "time": time(1), "description": "유럽쏙독새가 당신의 업적을 이야기합니다"},
            {"name": "칡부엉이", "time": time(1), "description": "칡부엉이가 당신을 좋아합니다"},
            {"name": "흰얼굴소쩍새", "time": time(1), "description": "흰얼굴소쩍새가 당신에게 푹 쉬라 해줍니다"},
            {"name": "아메리카올빼미", "time": time(1), "description": "아메리카올뻬미가 당신을 알아봅니다"},
            {"name": "큰수리부엉이", "time": time(1), "description": "큰수리부엉이가 당신의 열정에 힘입어 큰큰수리부엉이가 되었습니다"},

            {"name": "작은소쩍새", "time": time(2), "description": "작은소쩍새가 잠결에 당신의 대단한 모습을 봤습니다"},
            {"name": "잿빛올빼미", "time": time(2), "description": "잿빛올빼미도 당신을 놀라워합니다"},
            {"name": "늪올빼미", "time": time(2), "description": "늪올빼미가 당신의 시간에 감명받았습니다"},
            {"name": "호반새", "time": time(2), "description": "호반새가 당신을 보고 깊은 감동을 받았습니다"},
            {"name": "솔개", "time": time(2), "description": "솔개가 당신에게 힘을 불어넣어줍니다"},

            {"name": "뻐꾸기", "time": time(3), "description": "뻐꾸기는 당신을 보고 열심히 살기로 했습니다"},
            {"name": "종다리", "time": time(3), "description": "종다리는 당신을 따라가기로 합니다"},
            {"name": "붉은머리오목눈이", "time": time(3), "description": "붉은머리오목눈이는 당신만 바라봅니다"},
            {"name": "박새", "time": time(3), "description": "박새는 당신의 시간이 귀중했다는 것을 알고 있습니다"},
            {"name": "호랑지빠귀", "time": time(3), "description": "호랑지빠귀가 당신에게 박수를 쳐줍니다"},

            {"name": "진박새", "time": time(4), "description": "진박새가 당신을 진짜 박새라 인정합니다"},
            {"name": "곤줄박이", "time": time(4), "description": "곤줄박이가 당신의 열정을 느끼고 일찍 일어났습니다"},
            {"name": "동고비", "time": time(4), "description": "동고비들이 당신을 함께 칭찬합니다"},
            {"name": "퇴새", "time": time(4), "description": "퇴새가 당신이 최선을 다 한 모습이 아름답다 합니다"},
            {"name": "되지빠귀", "time": time(4), "description": "되지빠귀가 당신에게 긍정적인 영향을 받습니다"},

            {"name": "까치", "time": time(5), "description": "까치가 당신에게 행운을 줍니다"},
            {"name": "비둘기", "time": time(5), "description": "비둘기가 당신을 반겨줍니다"},
            {"name": "참새", "time": time(5), "description": "참새가 당신을 보고 다시 잡니다"},
            {"name": "물까치", "time": time(5), "description": "물까치가 당신에게 오늘도 힘내라 합니다"},
            {"name": "까마귀", "time": time(5), "description": "까마귀가 당신에게 행운을 줍니다"},

            {"name": "노란머리블랙버드", "time": time(6), "description": "노란머리블랙버드가 당신을 보고 검은머리가 되었습니다"},
            {"name": "기러기", "time": time(6), "description": "기러기가 당신을 보고 뒤집어져 기러기가 되었습니다"},
            {"name": "오리", "time": time(6), "description": "오리가 당신을 안아줍니다"},
            {"name": "해오라기", "time": time(6), "description": "해오라기는 당신을 기억할 것입니다"},
            {"name": "꿩", "time": time(6), "description": "꿩이 당신에게 오늘은 치킨을 먹으라 합니다"},

            {"name": "매", "time": time(7), "description": "매는 당신을 믿었습니다"},
            {"name": "꾀꼬리", "time": time(7), "description": "꾀꼬리가 당신을 위해 아름답게 웁니다"},
            {"name": "원앙", "time": time(7), "description": "원앙은 오늘부터 당신을 계속 믿을 것입니다"},
            {"name": "백로", "time": time(7), "description": "백로는 당신의 노력이 빛난다 합니다"},
            {"name": "흰이마딱새", "time": time(7), "description": "흰이마딱새가 당신을 축하하며 날갯짓을 합니다"},
        ]
        
        for book in birds:
            Bird.objects.create(**book)
        self.stdout.write(self.style.SUCCESS('reset and created birds data'))