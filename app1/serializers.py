from djoser.serializers import UserCreateSerializer
from .models import CustomUser, Files
from rest_framework.serializers import ModelSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ("id", "email", "username", "password")


class Files_Serialaizer(ModelSerializer):
    class Meta:
        model = Files
        fields = ('number', 'user', 'name', 'weight', 'extension', 'upload_date')


# class UserDataSerialaizer(ModelSerializer):
#     class Meta:
#         model = Files
#         fields = ('ip', 'lang', 'all_lang', 'plugins', 'browser', 'OS', 'display', 'cords')
