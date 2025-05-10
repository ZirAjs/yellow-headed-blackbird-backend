from rest_framework.response import Response
from accounts.models import Tier
from accounts.serializers import TierSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

@permission_classes([AllowAny])
class TierViewSet(APIView):
    def get(self, request):
        tiers = Tier.objects.all()
        serializer = TierSerializer(tiers, many=True)
        return Response(serializer.data)