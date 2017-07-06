# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.admin user.py
    ::moduledescription: user admin model
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "email",
        "first_name",
        "last_name"
    ]

    readonly_fields = [
        "uuid",
        "email"
    ]

admin.site.register(User, UserAdmin)
