from django.contrib import admin
from .models import CustomUser, Files

admin.site.register(CustomUser)
admin.site.register(Files)
