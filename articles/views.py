from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@permission_classes([AllowAny])
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ["get"]
