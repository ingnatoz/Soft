from django.contrib import admin
from .models import User


@admin.register(User)
class Buyer(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'last_name', 'email',)
    ordering = ('id',)
