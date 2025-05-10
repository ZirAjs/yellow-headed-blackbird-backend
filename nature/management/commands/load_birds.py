from django.core.management.base import BaseCommand
from nature.models import Bird
from datetime import time

class Command(BaseCommand):
    help = 'Load hardcoded bird data'

    def handle(self, *args, **kwargs):
        Bird.objects.all().delete()
        from datetime import time

        from datetime import time

        birds = [
            {"name": "참새", "time": time(0), "description": "참새가 밤의 고요 속, 나뭇가지에 옹기종기 모여 단잠을 잡니다."},
            {"name": "나이팅게일", "time": time(0), "description": "나이팅게일이 어둠 속에서 조용히 깃털을 다듬으며 새벽을 기다립니다."},
            {"name": "독수리", "time": time(0), "description": "독수리가 높은 둥지에서 달빛 아래 날개를 접고 휴식합니다."},
            {"name": "앵무새", "time": time(0), "description": "앵무새가 알록달록한 열매 꿈을 꾸며 곤히 잠든 밤입니다."},
            {"name": "한국 덤불 종달이", "time": time(0), "description": "한국 덤불 종달이가 밤의 추위 속, 덤불 속에 몸을 숨기고 따뜻함을 유지합니다."},

            {"name": "창백한 개똥지빠귀", "time": time(1), "description": "창백한 개똥지빠귀가 여명이 밝아오자 슬슬 기지개를 켭니다."},
            {"name": "일본 녹색 딱따구리", "time": time(1), "description": "일본 녹색 딱따구리가 어둠 속에서 아침 일찍 활동할 곤충 소리에 귀 기울입니다."},
            {"name": "말라드 오리", "time": time(1), "description": "말라드 오리가 고요한 물 위에서 평화롭게 떠 있는 밤입니다."},
            {"name": "회색 왜가리", "time": time(1), "description": "회색 왜가리가 미동 없이 서서, 방심한 물고기를 기다리는 새벽입니다."},
            {"name": "동점박이 오리", "time": time(1), "description": "동점박이 오리가 부드러운 새벽의 합창을 조용히 시작합니다."},

            {"name": "소쩍새", "time": time(2), "description": "소쩍새의 밤의 울음소리가 새벽의 고요함 속으로 스며드는 시간입니다."},
            {"name": "딱따구리", "time": time(2), "description": "딱따구리가 나무 줄기에 규칙적인 드럼 연주를 시작하는 아침입니다."},
            {"name": "매", "time": time(2), "description": "매가 조용히 날갯짓하며, 깨어나는 풍경을 살핍니다."},
            {"name": "까마귀", "time": time(2), "description": "까마귀가 요란한 울음소리로 하루의 시작을 알립니다."},
            {"name": "핀치", "time": time(2), "description": "핀치가 가지 사이를 팔짝이며, 즐거운 아침 인사를 건넵니다."},

            {"name": "비둘기", "time": time(3), "description": "비둘기가 도시 광장에 모여 아침 식사를 찾아 분주합니다."},
            {"name": "오리", "time": time(3), "description": "오리가 잔잔한 물결을 일으키며 연못을 헤엄치는 아침의 여유를 즐깁니다."},
            {"name": "펠리컨", "time": time(3), "description": "펠리컨이 커다란 날개를 펴고 아침 비행을 준비하는 거대한 날갯짓을 합니다."},
            {"name": "제비", "time": time(3), "description": "제비가 하늘을 가르며, 아침 일찍 날아다니는 곤충을 잡는 날렵함을 보여줍니다."},
            {"name": "황새", "time": time(3), "description": "황새가 얕은 물가에서 장엄하게 거니는 새벽의 우아함을 뽐냅니다."},

            {"name": "올빼미", "time": time(4), "description": "올빼미가 밤의 사냥을 마치고 보금자리로 돌아가는 은밀한 발걸음을 옮깁니다."},
            {"name": "물총새", "time": time(4), "description": "물총새가 인내심을 가지고 앉아, 물속의 번쩍이는 은빛을 기다리는 새벽의 눈빛을 보냅니다."},
            {"name": "거위", "time": time(4), "description": "거위가 시끄럽게 울며 넓은 들판에서 풀을 뜯는 아침의 활기를 보여줍니다."},
            {"name": "로빈", "time": time(4), "description": "로빈이 아름다운 아침 노래로 하루를 깨우는 작은 음악가입니다."},
            {"name": "솔개", "time": time(4), "description": "솔개가 높이 원을 그리며, 먹이를 찾아 하늘을 맴도는 날카로운 시선을 던집니다."},

            {"name": "참새", "time": time(5), "description": "참새가 분주하게 씨앗과 곤충을 찾아다니는 활기찬 아침을 맞이합니다."},
            {"name": "나이팅게일", "time": time(5), "description": "나이팅게일이 복잡하고 아름다운 노래로 새벽을 물들입니다."},
            {"name": "독수리", "time": time(5), "description": "독수리가 날카로운 눈으로 아침 식사를 사냥하는 하늘의 제왕입니다."},
            {"name": "앵무새", "time": time(5), "description": "앵무새가 나뭇가지 위에서 시끄럽게 재잘거리는 수다쟁이입니다."},
            {"name": "한국 덤불 종달이", "time": time(5), "description": "한국 덤불 종달이가 덤불 속을 빠르게 움직이며 먹이를 찾는 작은 몸짓을 보입니다."},

            {"name": "창백한 개똥지빠귀", "time": time(6), "description": "창백한 개똥지빠귀가 떠오르는 태양의 따스함을 즐기는 평화로운 아침입니다."},
            {"name": "일본 녹색 딱따구리", "time": time(6), "description": "일본 녹색 딱따구리가 나무껍질에서 곤충을 끈기 있게 찾는 부리를 움직입니다."},
            {"name": "말라드 오리", "time": time(6), "description": "말라드 오리가 활발하게 헤엄치며 먹이를 찾는 아침의 분주함을 보입니다."},
            {"name": "회색 왜가리", "time": time(6), "description": "회색 왜가리가 느리고 신중한 날갯짓으로 하늘을 나는 우아함을 뽐냅니다."},
            {"name": "동점박이 오리", "time": time(6), "description": "동점박이 오리가 둥지를 짓거나 보살피는 사랑스러운 모습을 보여줍니다."},

            {"name": "소쩍새", "time": time(7), "description": "소쩍새가 그늘진 곳에서 깊은 잠에 빠진 밤의 사냥꾼입니다."},
            {"name": "딱따구리", "time": time(7), "description": "딱따구리가 둥지를 틀기 위해 열심히 나무에 구멍을 파는 중입니다."},
            {"name": "매", "time": time(7), "description": "매가 높은 나뭇가지에 앉아 자신의 영역을 조용히 감시하는 매의 눈빛을 보냅니다."},
            {"name": "까마귀", "time": time(7), "description": "까마귀가 땅바닥의 반짝이는 무언가를 호기심 가득하게 조사하는 중입니다."},
            {"name": "핀치", "time": time(7), "description": "핀치가 햇살 가득한 곳에서 씨앗을 맛있게 쪼아 먹는 작은 행복을 누립니다."},

            {"name": "비둘기", "time": time(8), "description": "비둘기가 지붕 위를 자신감 넘치게 걸어 다니는 도시의 터줏대감입니다."},
            {"name": "오리", "time": time(8), "description": "오리가 꼬리를 하늘로 향하고 물속에서 먹이를 찾는 즐거운 몸짓을 합니다."},
            {"name": "펠리컨", "time": time(8), "description": "펠리컨이 잔잔한 물 위를 우아하게 활공하는 거대한 날개를 펼칩니다."},
            {"name": "제비", "time": time(8), "description": "제비가 하늘 높이 날아오르며 공중에서 곤충을 잡는 곡예사입니다."},
            {"name": "황새", "time": time(8), "description": "황새가 습지 위를 느릿하게 날아가는 장엄한 모습을 보여줍니다."},

            {"name": "올빼미", "time": time(9), "description": "올빼미가 낮 동안 조용히 숨어 잠을 자는 밤의 현자입니다."},
            {"name": "물총새", "time": time(9), "description": "물총새가 나뭇가지에서 번개처럼 튀어나와 물속으로 다이빙하는 순간을 포착합니다."},
            {"name": "거위", "time": time(9), "description": "거위가 아장아장 걷는 아기 거위들을 이끄는 든든한 엄마의 모습을 보여줍니다."},
            {"name": "로빈", "time": time(9), "description": "로빈이 부지런히 땅속에서 지렁이를 찾아내는 붉은 가슴을 내밉니다."},
            {"name": "솔개", "time": time(9), "description": "솔개가 잠시 공중에서 멈췄다가 먹이를 향해 급강하하는 날카로운 발톱을 드러냅니다."},

            {"name": "참새", "time": time(10), "description": "참새가 나뭇잎 사이에서 지저귀는 작고 활기찬 목소리를 냅니다."},
            {"name": "나이팅게일", "time": time(10), "description": "나이팅게일이 높은 곳에서 울려 퍼지는 감미로운 노래의 향연을 선사합니다."},
            {"name": "독수리", "time": time(10), "description": "독수리가 잡은 먹이를 둥지로 가져가는 힘찬 날갯짓을 합니다."},
            {"name": "앵무새", "time": time(10), "description": "앵무새가 주변에서 들리는 소리를 흉내 내는 재능 있는 성대모사꾼입니다."},
            {"name": "한국 덤불 종달이", "time": time(10), "description": "한국 덤불 종달이가 빽빽한 덤불 속에서 먹이를 찾는 섬세한 움직임을 보입니다."},

            {"name": "푸른 어치", "time": time(11), "description": "푸른 어치가 밝은 햇살 아래 당당하게 도토리를 찾는 푸른 깃털을 뽐냅니다."},
            {"name": "추기경새", "time": time(11), "description": "추기경새가 푸른 잎사귀 사이로 강렬한 붉은색 섬광을 뽐내는 아름다움을 자랑합니다."},
            {"name": "벌새", "time": time(11), "description": "벌새가 꽃에서 꽃으로 쏜살같이 날아다니며 꿀을 빠는 작은 요정 같습니다."},
            {"name": "흉내지빠귀", "time": time(11), "description": "흉내지빠귀가 자신만의 레퍼토리로 다른 새들의 울음소리를 흉내 내는 재주꾼입니다."},
            {"name": "비둘기", "time": time(11), "description": "비둘기가 전화선에 평화롭게 앉아 구구거리는 오후의 여유를 즐깁니다."},
            # 12시
            {"name": "물수리", "time": time(12), "description": "물수리가 물 위를 높이 맴돌다 물고기를 향해 급강하할 준비 태세를 갖춥니다."},
            {"name": "종달이", "time": time(12), "description": "종달이가 하늘 높이 날아올라 맑고 드높은 멜로디를 노래하는 하늘의 음유시인입니다."},
            {"name": "칼새", "time": time(12), "description": "칼새가 믿을 수 없는 속도로 날아다니며 공중에서 곤충을 잡는 날렵한 사냥꾼입니다."},
            {"name": "말똥가리", "time": time(12), "description": "말똥가리가 상승 기류를 타고 느긋하게 하늘을 나는 오후의 유람자입니다."},
            {"name": "메추라기", "time": time(12), "description": "메추라기가 키 큰 풀 속에 숨어 부드러운 울음소리를 내는 수줍은 존재입니다."},
            # 13시
            {"name": "왜가리", "time": time(13), "description": "왜가리가 물가에서 꼼짝 않고 먹이를 기다리는 인내심 강한 사냥꾼입니다."},
            {"name": "물총새", "time": time(13), "description": "물총새가 시냇가 위 나뭇가지에 가만히 앉아 때를 기다리는 푸른 보석 같습니다."},
            {"name": "어치", "time": time(13), "description": "어치가 높은 나뭇가지에서 시끄럽게 꾸짖는 숲의 감시자입니다."},
            {"name": "찌르레기", "time": time(13), "description": "찌르레기가 크고 시끄러운 무리를 지어 모이는 활기 넘치는 군집을 이룹니다."},
            {"name": "굴뚝새", "time": time(13), "description": "굴뚝새가 엉킨 덤불 속을 바쁘게 돌아다니며 먹이를 찾는 작은 에너지입니다."},
            # 14시
            {"name": "백로", "time": time(14), "description": "백로가 얕은 물가를 우아하게 걸어 다니는 순백의 아름다움입니다."},
            {"name": "도요새", "time": time(14), "description": "도요새가 해변을 따라 뛰어다니며 부리로 모래를 탐색하는 작은 발걸음을 보입니다."},
            {"name": "개똥지빠귀", "time": time(14), "description": "개똥지빠귀가 숨겨진 횃대에서 풍부하고 부드러운 노래를 들려주는 숲의 음악가입니다."},
            {"name": "황금방울새", "time": time(14), "description": "황금방울새가 엉겅퀴 씨앗을 먹으며 노란 날개를 반짝이는 아름다움을 뽐냅니다."},
            {"name": "피비", "time": time(14), "description": "피비가 낮은 나뭇가지에 앉아 꼬리를 가볍게 흔드는 조용한 관찰자입니다."},
            # 15시
            {"name": "황조롱이", "time": time(15), "description": "황조롱이가 바람 속에서 정지 비행하며 작은 포유류를 찾는 매의 눈빛을 보냅니다."},
            {"name": "동고비", "time": time(15), "description": "동고비가 나무 줄기를 거꾸로 내려오며 먹이를 찾는 독특한 움직임을 보입니다."},
            {"name": "박새", "time": time(15), "description": "박새가 맛있는 씨앗을 찾아 거꾸로 매달리는 재주꾼입니다."},
            {"name": "토히", "time": time(15), "description": "토히가 낙엽 속을 힘차게 긁어대며 먹이를 찾는 열정적인 탐색가입니다."},
            {"name": "그래클", "time": time(15), "description": "그래클이 햇빛 아래 반짝이는 검은 깃털을 뽐내며 잔디밭을 걷는 당당한 모습입니다."},
            # 16시
            {"name": "때까치", "time": time(16), "description": "때까치가 가시덤불에 앉아 주변을 경계하는 날카로운 시선을 던집니다."},
            {"name": "청둥오리", "time": time(16), "description": "청둥오리가 얕은 연못에 머리를 담그고 먹이를 찾는 평화로운 모습입니다."},
            {"name": "가마우지", "time": time(16), "description": "가마우지가 바위 위에 서서 날개를 활짝 펴고 말리는 중입니다."},
            {"name": "까치", "time": time(16), "description": "까치가 둥지를 짓기 위해 나뭇가지를 모으는 분주한 움직임을 보입니다."},
            {"name": "준코", "time": time(16), "description": "준코가 떨어진 씨앗을 찾아 땅바닥을 쪼는 작은 부리를 움직입니다."},
            # 17시
            {"name": "우드콕", "time": time(17), "description": "우드콕이 황혼 무렵 하늘에서 독특한 춤을 추기 시작하는 신비로운 새입니다."},
            {"name": "휘퍼윌", "time": time(17), "description": "휘퍼윌이 어스름이 깔리자 특유의 울음소리를 내기 시작하는 밤의 전령입니다."},
            {"name": "갈색 지빠귀", "time": time(17), "description": "갈색 지빠귀가 긴 부리로 낙엽을 헤집으며 먹이를 찾는 섬세한 탐색을 합니다."},
            {"name": "벨트 물총새", "time": time(17), "description": "벨트 물총새가 날아가며 딸랑거리는 울음소리를 내는 활기찬 모습입니다."},
            {"name": "붉은가슴방울새", "time": time(17), "description": "붉은가슴방울새가 버드나무 꽃가지에 매달려 씨앗을 먹는 작은 솜털 공 같습니다."},
            # 18시
            {"name": "헛간 제비", "time": time(18), "description": "헛간 제비가 저녁 어스름 속, 들판 위를 낮게 납니다."},
            {"name": "미국 비턴", "time": time(18), "description": "미국 비턴이 갈대밭 사이에 꼼짝없이 서 있는 위장술의 달인입니다."},
            {"name": "Common Nighthawk", "time": time(18), "description": "Common Nighthawk이 황혼 하늘에서 곤충을 사냥하는 밤의 사냥꾼입니다."},
            {"name": "은둔자 지빠귀", "time": time(18), "description": "은둔자 지빠귀가 황홀한 저녁 노래를 조용히 들려주는 숲 속의 은둔자입니다."},
            {"name": "저녁 울새", "time": time(18), "description": "저녁 울새가 해 질 녘, 모이통에 모여드는 노란 아름다움입니다."},
            # 19시
            {"name": "큰뿔올빼미", "time": time(19), "description": "큰뿔올빼미가 어둠이 내리자 부드럽게 울음소리를 내는 밤의 제왕입니다."},
            {"name": "Common Poorwill", "time": time(19), "description": "Common Poorwill이 어둑한 불빛 속에서 반복적인 울음소리를 냅니다."},
            {"name": "Eastern Whip-poor-will", "time": time(19), "description": "Eastern Whip-poor-will이 밤의 장막 아래, 숲 속에서 또렷한 울음소리를 반복합니다."},
            {"name": "바늘꼬리칼새", "time": time(19), "description": "바늘꼬리칼새가 어둠 속에서도 빠른 속도로 하늘을 가르며 날아다닙니다."},
            {"name": "흰뺨오리", "time": time(19), "description": "흰뺨오리가 어두워진 호수 위를 조용히 떠다니는 밤의 평화로운 풍경입니다."},
            # 20시
            {"name": "수리부엉이", "time": time(20), "description": "수리부엉이가 어둠 속에서 강력한 발톱으로 먹이를 사냥하는 밤의 지배자입니다."},
            {"name": "올빼미", "time": time(20), "description": "올빼미가 조용히 날갯짓하며 밤의 숲 속을 누비는 신비로운 존재입니다."},
            {"name": "쏙독새", "time": time(20), "description": "쏙독새가 밤하늘을 가르며 독특한 울음소리를 내는 밤의 방문객입니다."},
            {"name": "박쥐매", "time": time(20), "description": "박쥐매가 어둠 속에서 날렵하게 박쥐를 쫓는 밤의 사냥꾼입니다."},
            {"name": "검은머리물떼새", "time": time(20), "description": "검은머리물떼새가 어두운 해변가에서 조용히 먹이를 찾는 밤의 해안가 주민입니다."},
            # 21시
            {"name": "칡부엉이", "time": time(21), "description": "칡부엉이가 어둠 속에서 낮은 울음소리로 영역을 알리는 밤의 소리꾼입니다."},
            {"name": "별나비", "time": time(21), "description": "별나비가 희미한 달빛 아래 밤의 정원을 조용히 날아다니는 밤의 나비입니다."},
            {"name": "양비둘기", "time": time(21), "description": "양비둘기가 어두운 둥지에서 조용히 휴식을 취하는 밤의 평화로운 모습입니다."},
            {"name": "쇠부엉이", "time": time(21), "description": "쇠부엉이가 어둠 속에서 작은 포유류를 찾아 조용히 날아다니는 밤의 사냥꾼입니다."},
            {"name": "붉은발도요", "time": time(21), "description": "붉은발도요가 어두운 갯벌에서 긴 부리로 조용히 먹이를 찾는 밤의 탐색가입니다."},
            # 22시
            {"name": "흰올빼미", "time": time(22), "description": "흰올빼미가 어둠 속에서 하얀 깃털을 빛내며 먹이를 찾는 북극의 사냥꾼입니다."},
            {"name": "밤꾀꼬리", "time": time(22), "description": "밤꾀꼬리가 어두운 밤, 숨겨진 곳에서 아름다운 노랫소리를 들려주는 밤의 음악가입니다."},
            {"name": "회색머리아비", "time": time(22), "description": "회색머리아비가 어두운 호수 위에서 조용히 잠을 청하는 밤의 호수 거주자입니다."},
            {"name": "검은댕기해오라기", "time": time(22), "description": "검은댕기해오라기가 어두운 밤, 물가에서 조용히 먹이를 기다리는 밤의 사냥꾼입니다."},
            {"name": "뿔종다리", "time": time(22), "description": "뿔종다리가 어두운 들판에서 조용히 몸을 숨기고 밤을 보내는 들판의 주민입니다."},
            # 23시
            {"name": "솔부엉이", "time": time(23), "description": "솔부엉이가 깊은 밤, 숲 속에서 구슬픈 울음소리를 내는 밤의 슬픈 노래꾼입니다."},
            {"name": "작은 부엉이", "time": time(23), "description": "작은 부엉이가 어둠 속에서 큰 눈을 빛내며 주변을 경계하는 밤의 작은 감시자입니다."},
            {"name": "멧도요", "time": time(23), "description": "멧도요가 어두운 밤, 습지에서 독특한 소리를 내며 활동하는 밤의 습지 주민입니다."},
            {"name": "검은물떼새", "time": time(23), "description": "검은물떼새가 어두운 해안가 바위 위에서 조용히 밤을 보내는 밤의 해안가 주민입니다."},
            {"name": "북방쇠박새", "time": time(23), "description": "북방쇠박새가 어두운 숲 속 나뭇가지에 매달려 조용히 밤을 맞이하는 숲의 작은 주민입니다."},
        ]
        
        for book in birds:
            Bird.objects.create(**book)
        self.stdout.write(self.style.SUCCESS('reset and created birds data'))