from rest_framework.response import Response
from accounts.models import Cutoff
from accounts.serializers import CutoffSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

@permission_classes([AllowAny])
class CutoffViewSet(APIView):
    def get(self, request):
        cutoffs = Cutoff.objects.all()
        serializer = CutoffSerializer(cutoffs, many=True)
        return Response(serializer.data)