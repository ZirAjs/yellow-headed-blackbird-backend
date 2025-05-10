from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, min_length=8, max_length=20
    )

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        # Store user for use in the view
        data["user"] = user
        return data

    class Meta:
        model = User
        fields = ["username", "password"]


class CreateUserSerializer(BaseUserSerializer):
    nickname = serializers.CharField(required=True, min_length=2, max_length=20)

    def validate(self, data):
        # Check if the username already exists
        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("Username already exists.")

        # Check if the nickname already exists
        if User.objects.filter(nickname=data["nickname"]).exists():
            raise serializers.ValidationError("Nickname already exists.")

        # Check if the password is strong enough (example: at least 8 characters)
        if len(data["password"]) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )

        return data

    def create(self, validated_data):
        user = User(
            username=validated_data["username"], nickname=validated_data["nickname"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = BaseUserSerializer.Meta.fields + ["nickname"]


class UpdateUserSerializer(BaseUserSerializer):
    nickname = serializers.CharField(required=True, min_length=2, max_length=20)

    def validate(self, data):
        # Check if the nickname already exists
        if User.objects.filter(nickname=data["nickname"]).exists():
            raise serializers.ValidationError("Nickname already exists.")

        return data

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ["nickname"]
