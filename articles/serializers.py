from rest_framework.serializers import ModelSerializer
from .models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
