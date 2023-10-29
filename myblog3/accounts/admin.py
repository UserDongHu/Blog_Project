from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'nickname', 'posting_num', 'reply_num')

admin.site.register(MyUser, MyUserAdmin)