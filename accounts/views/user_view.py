from rest_framework import viewsets, mixins
from accounts.models import User
from accounts.serializers import CreateUserSerializer, UpdateUserSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    lookup_field = "id"
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == "retrieve":
            return [AllowAny()]
        elif self.action == "me":
            return [IsAuthenticated()]
        return [IsAuthenticated()]  # default fallback

    @action(detail=False, methods=["get", "put"])
    def me(self, request, *args, **kwargs):
        """
        내 정보 조회 및 수정 API
        """
        match request.method:
            case "GET":
                seralizer = CreateUserSerializer(data=request.user)

                return Response(seralizer.data)

            case "PUT":
                user = request.user
                serializer_new = UpdateUserSerializer(data=request.data)
                serializer_new.is_valid(raise_exception=True)

                user.nickname = serializer_new.validated_data["nickname"]
                return Response(serializer_new.data)
