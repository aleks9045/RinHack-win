from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return str(self.id)


class Files(models.Model):
    number = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField('name', max_length=255)
    weight = models.IntegerField('weight')
    extension = models.CharField('extension', max_length=18)
    upload_date = models.DateTimeField('date', auto_now=True)

    def __str__(self):
        return str(self.user)


class UserData(models.Model):
    ip = models.CharField(max_length=32)
    lang = models.CharField(max_length=64)
    all_lang = models.CharField(max_length=2048)
    plugins = models.CharField(max_length=2048)
    browser = models.CharField(max_length=64)
    OS = models.CharField(max_length=64)
    display = models.CharField(max_length=16)
    cords = models.CharField(max_length=64)

    def __str__(self):
        return str(self.ip)
