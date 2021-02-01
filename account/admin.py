from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'Born', 'photo', 'Job', 'Education')


# Register your models here.
