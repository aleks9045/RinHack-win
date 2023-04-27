from django.contrib import admin
from .models import CustomUser, Files, UserData

admin.site.register(CustomUser)
admin.site.register(Files)
admin.site.register(UserData)