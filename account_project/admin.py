from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo')
