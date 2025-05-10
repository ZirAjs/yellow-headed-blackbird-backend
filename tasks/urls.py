from django.urls import path
from .views import GenerateTasksView

urlpatterns = [
    path("create-tasks/", GenerateTasksView.as_view(), name="create-tasks"),
]
