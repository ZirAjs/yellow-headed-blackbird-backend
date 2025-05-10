from django.urls import path
from .views import NatureEventsView

urlpatterns = [
    path("nature-events/", NatureEventsView.as_view(), name="nature-events"),
]
