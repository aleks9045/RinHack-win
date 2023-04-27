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
        return str(self.username)


class UserUser(models.Model):
    username = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    fp = models.TextField(blank=True)

    def __str__(self):
        return str(self.username)


class Files(models.Model):
    email = models.CharField(max_length=32, blank=True)
    name = models.CharField('name', max_length=255, blank=True)
    weight = models.IntegerField('weight', blank=True)
    extension = models.CharField('extension', max_length=18, blank=True)
    upload_date = models.DateTimeField('date', auto_now=True, blank=True)

    def __str__(self):
        return str(self.email)


class Hshs(models.Model):
    fp = models.TextField()

    def __str__(self):
        return str(self.fp)