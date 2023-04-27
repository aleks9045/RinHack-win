from django.contrib import admin
from .models import CustomUser, Files, Hshs, UserUser

admin.site.register(CustomUser)
admin.site.register(Files)
admin.site.register(Hshs)
admin.site.register(UserUser)
