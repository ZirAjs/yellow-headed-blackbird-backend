from django.core.management.base import BaseCommand
from accounts.models import Cutoff

class Command(BaseCommand):
    help = 'Load Cutoff Data'

    def handle(self, *args, **kwargs):
        Cutoff.objects.all().delete()

        cutoffs = [
            {'name': '새싹', 'cut': 100},
            {'name': '줄기', 'cut': 200},
            {'name': '꽃', 'cut': 300},
            {'name': '나무', 'cut': 400},
            {'name': '숲', 'cut': 500},
        ]
        for cutoff in cutoffs:
            Cutoff.objects.create(**cutoff)
        self.stdout.write(self.style.SUCCESS('all cut loaded'))