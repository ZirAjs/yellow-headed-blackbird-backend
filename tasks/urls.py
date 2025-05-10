from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenerateTasksView

router = DefaultRouter()
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("create-tasks/", GenerateTasksView.as_view(), name="create-tasks"),
]
