from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiaryViewSet

router = DefaultRouter()
router.register(r"diaries", DiaryViewSet, basename="diaries")
urlpatterns = [
    path("", include(router.urls)),
]
