from djoser.serializers import UserCreateSerializer
from .models import CustomUser, Files, UserUser
from rest_framework.serializers import ModelSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ("id", "email", "username", "password")


class Files_Serialaizer(ModelSerializer):
    class Meta:
        model = Files
        fields = ('email', 'name', 'weight', 'extension', 'upload_date')


class UserUserSerialaizer(ModelSerializer):
    class Meta:
        model = UserUser
        fields = ("username", "email", "fp")
