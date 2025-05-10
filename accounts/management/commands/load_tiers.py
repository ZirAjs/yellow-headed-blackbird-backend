from django.core.management.base import BaseCommand
from accounts.models import Tier

class Command(BaseCommand):
    help = 'Load Tier Data'

    def handle(self, *args, **kwargs):
        Tier.objects.all().delete()

        tiers = [
            {'name': '새싹', 'cut': 100},
            {'name': '줄기', 'cut': 200},
            {'name': '꽃', 'cut': 300},
            {'name': '나무', 'cut': 400},
            {'name': '숲', 'cut': 500},
        ]
        for tier in tiers:
            Tier.objects.create(**tier)
        self.stdout.write(self.style.SUCCESS('all tier loaded'))