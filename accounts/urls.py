from django.urls import path, include
from accounts.views.auth_view import RegisterView, LoginView
from rest_framework.routers import DefaultRouter
from accounts.views.user_view import UserViewSet

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
