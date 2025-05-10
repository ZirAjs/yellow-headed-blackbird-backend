# 일반적으로 REST API에서는 reste_framework.views 대신 rest_framework.generics에 정의된 GenericAPIView를 사용한다.
from rest_framework.generics import GenericAPIView, CreateAPIView
from accounts.serializers import BaseUserSerializer, CreateUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


@permission_classes([AllowAny])
class RegisterView(CreateAPIView):
    """
    회원가입 API
    """

    serializer_class = CreateUserSerializer  # 회원가입 시 사용할 Serializer를 지정한다.


@permission_classes([AllowAny])
class LoginView(GenericAPIView):
    """
    로그인 API
    """

    serializer_class = BaseUserSerializer  # 로그인 시 사용할 Serializer를 지정한다.

    def post(self, request, *args, **kwargs):
        # serializer 사용하여 요청 데이터 검증
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)  # RefreshToken 생성
        response = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(response)
