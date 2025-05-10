from django.core.management.base import BaseCommand
from nature.models import Bird
from datetime import time

class Command(BaseCommand):
    help = 'Load hardcoded bird data'

    def handle(self, *args, **kwargs):
        Bird.objects.all().delete()
        from datetime import time

        from datetime import time

        from datetime import time

        birds = [
            {"name": "헛간올빼미", "time": time(0), "description": ""},
            {"name": "수리부엉이", "time": time(0), "description": ""},
            {"name": "올빼미", "time": time(0), "description": ""},
            {"name": "검은관해오라기", "time": time(0), "description": ""},
            {"name": "나이팅게일", "time": time(0), "description": ""},

            {"name": "유럽쏙독새", "time": time(1), "description": ""},
            {"name": "칡부엉이", "time": time(1), "description": ""},
            {"name": "흰얼굴소쩍새", "time": time(1), "description": ""},
            {"name": "아메리카올빼미", "time": time(1), "description": ""},
            {"name": "큰수리부엉이", "time": time(1), "description": ""},

            {"name": "작은소쩍새", "time": time(2), "description": ""},
            {"name": "잿빛올빼미", "time": time(2), "description": ""},
            {"name": "늪올빼미", "time": time(2), "description": ""},
            {"name": "호반새", "time": time(2), "description": ""},
            {"name": "솔개", "time": time(2), "description": ""},

            {"name": "뻐꾸기", "time": time(3), "description": ""},
            {"name": "종다리", "time": time(3), "description": ""},
            {"name": "붉은머리오목눈이", "time": time(3), "description": ""},
            {"name": "박새", "time": time(3), "description": ""},
            {"name": "호랑지빠귀", "time": time(3), "description": ""},

            {"name": "진박새", "time": time(4), "description": ""},
            {"name": "곤줄박이", "time": time(4), "description": ""},
            {"name": "동고비", "time": time(4), "description": ""},
            {"name": "퇴새", "time": time(4), "description": ""},
            {"name": "되지빠귀", "time": time(4), "description": ""},

            {"name": "까치", "time": time(5), "description": ""},
            {"name": "비둘기", "time": time(5), "description": ""},
            {"name": "참새", "time": time(5), "description": ""},
            {"name": "물까치", "time": time(5), "description": ""},
            {"name": "까마귀", "time": time(5), "description": ""},

            {"name": "노란머리블랙버드", "time": time(6), "description": ""},
            {"name": "기러기", "time": time(6), "description": ""},
            {"name": "오리", "time": time(6), "description": ""},
            {"name": "해오라기", "time": time(6), "description": ""},
            {"name": "꿩", "time": time(6), "description": ""},

            {"name": "매", "time": time(7), "description": ""},
            {"name": "꾀꼬리", "time": time(7), "description": ""},
            {"name": "원앙", "time": time(7), "description": ""},
            {"name": "백로", "time": time(7), "description": ""},
            {"name": "흰이마딱새", "time": time(7), "description": ""},

            {"name": "독수리", "time": time(8), "description": ""},
            {"name": "황조롱이", "time": time(8), "description": ""},
            {"name": "물총새", "time": time(8), "description": ""},
            {"name": "두루미", "time": time(8), "description": ""},
            {"name": "참매", "time": time(8), "description": ""},

            {"name": "갈매기", "time": time(9), "description": ""},
            {"name": "제비갈매기", "time": time(9), "description": ""},
            {"name": "도요새", "time": time(9), "description": ""},
            {"name": "물떼새", "time": time(9), "description": ""},
            {"name": "찌르레기", "time": time(9), "description": ""},

            {"name": "종다리", "time": time(10), "description": ""},
            {"name": "후루티", "time": time(10), "description": ""},
            {"name": "오색딱따구리", "time": time(10), "description": ""},
            {"name": "어치", "time": time(10), "description": ""},
            {"name": "방울새", "time": time(10), "description": ""},

            {"name": "뱀눈새", "time": time(11), "description": ""},
            {"name": "말똥가리", "time": time(11), "description": ""},
            {"name": "쏙독새", "time": time(11), "description": ""},
            {"name": "꾀꼬리매", "time": time(11), "description": ""},
            {"name": "할미새", "time": time(11), "description": ""},
            # Hour 12
            {"name": "솔개", "time": time(12), "description": ""},
            {"name": "황새", "time": time(12), "description": ""},
            {"name": "저어새", "time": time(12), "description": ""},
            {"name": "댕기물떼새", "time": time(12), "description": ""},
            {"name": "멧비둘기", "time": time(12), "description": ""},
            # Hour 13
            {"name": "금눈쇠오리", "time": time(13), "description": ""},
            {"name": "흰뺨검둥오리", "time": time(13), "description": ""},
            {"name": "큰기러기", "time": time(13), "description": ""},
            {"name": "노랑턱멧새", "time": time(13), "description": ""},
            {"name": "앵무새", "time": time(13), "description": ""},
            # Hour 14
            {"name": "토코투칸", "time": time(14), "description": ""},
            {"name": "솔잣새", "time": time(14), "description": ""},
            {"name": "붉은배새매", "time": time(14), "description": ""},
            {"name": "때까치", "time": time(14), "description": ""},
            {"name": "검독수리", "time": time(14), "description": ""},
            # Hour 15
            {"name": "오목눈이", "time": time(15), "description": ""},
            {"name": "동고비", "time": time(15), "description": ""},
            {"name": "딱따구리", "time": time(15), "description": ""},
            {"name": "물총새", "time": time(15), "description": ""},
            {"name": "큰유리새", "time": time(15), "description": ""},
            # Hour 16
            {"name": "찌르레기", "time": time(16), "description": ""},
            {"name": "방울새", "time": time(16), "description": ""},
            {"name": "흑고니", "time": time(16), "description": ""},
            {"name": "쇠기러기", "time": time(16), "description": ""},
            {"name": "흰눈썹황금새", "time": time(16), "description": ""},
            # Hour 17
            {"name": "백로", "time": time(17), "description": ""},
            {"name": "기러기", "time": time(17), "description": ""},
            {"name": "검은머리촉새", "time": time(17), "description": ""},
            {"name": "뜸새", "time": time(17), "description": ""},
            {"name": "쇠딱따구리", "time": time(17), "description": ""},
            # Hour 18
            {"name": "청둥오리", "time": time(18), "description": ""},
            {"name": "개개비", "time": time(18), "description": ""},
            {"name": "논병아리", "time": time(18), "description": ""},
            {"name": "검은댕기해오라기", "time": time(18), "description": ""},
            {"name": "뜸부기", "time": time(18), "description": ""},
            # Hour 19
            {"name": "큰소쩍새", "time": time(19), "description": ""},
            {"name": "아프리카올빼미", "time": time(19), "description": ""},
            {"name": "검은어깨매", "time": time(19), "description": ""},
            {"name": "갈색선개구리매", "time": time(19), "description": ""},
            {"name": "쇠올빼미", "time": time(19), "description": ""},
            # Hour 20
            {"name": "줄무늬올빼미", "time": time(20), "description": ""},
            {"name": "흰죽지수리", "time": time(20), "description": ""},
            {"name": "칡부엉이", "time": time(20), "description": ""},
            {"name": "긴꼬리딱새", "time": time(20), "description": ""},
            {"name": "기름쏙독새", "time": time(20), "description": ""},
            # Hour 21
            {"name": "밤도요", "time": time(21), "description": ""},
            {"name": "물닭", "time": time(21), "description": ""},
            {"name": "논병아리", "time": time(21), "description": ""},
            {"name": "검은댕기해오라기", "time": time(21), "description": ""},
            {"name": "큰부리소쩍새", "time": time(21), "description": ""},
            # Hour 22
            {"name": "인도수리부엉이", "time": time(22), "description": ""},
            {"name": "아메리카황새", "time": time(22), "description": ""},
            {"name": "따오기", "time": time(22), "description": ""},
            {"name": "큰소쩍새", "time": time(22), "description": ""},
            {"name": "유럽쏙독새", "time": time(22), "description": ""},
            # Hour 23
            {"name": "흰목올빼미", "time": time(23), "description": ""},
            {"name": "동굴올빼미", "time": time(23), "description": ""},
            {"name": "콘도르", "time": time(23), "description": ""},
            {"name": "짧은귀올빼미", "time": time(23), "description": ""},
            {"name": "호랑지빠귀", "time": time(23), "description": ""},
        ]
        
        for book in birds:
            Bird.objects.create(**book)
        self.stdout.write(self.style.SUCCESS('reset and created birds data'))