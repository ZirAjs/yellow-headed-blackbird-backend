from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import User, Setting, Tier


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ["alarm", "alarm_ui"]

class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = '__all__'

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
        Setting.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ["username", "nickname"]


class UpdateUserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(required=True, min_length=2, max_length=20)
    setting = SettingSerializer()

    def validate(self, value):
        user = self.context["request"].user
        if User.objects.filter(nickname=value).exclude(pk=user.pk).exists():
            raise serializers.ValidationError("Nickname already exists.")
        return value

    def update(self, instance, validated_data):
        setting_data = validated_data.pop("setting", None)

        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.save()

        if setting_data:
            for attr, value in setting_data.items():
                setattr(instance.setting, attr, value)
            instance.setting.save()

        return instance

    class Meta:
        model = User
        fields = ["nickname", "setting"]


class ViewUserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(required=True, min_length=2, max_length=20)
    setting = SettingSerializer()

    def validate(self, value):
        user = self.instance
        if User.objects.filter(nickname=value).exclude(pk=user.pk).exists():
            raise serializers.ValidationError("Nickname already exists.")
        return value

    def update(self, instance, validated_data):
        setting_data = validated_data.pop("setting", None)

        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.save()

        if setting_data:
            for attr, value in setting_data.items():
                setattr(instance.setting, attr, value)
            instance.setting.save()

        return instance

    class Meta:
        model = User
        fields = ["username", "nickname", "setting", "experience"]
