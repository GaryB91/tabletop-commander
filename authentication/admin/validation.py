# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.admin validation.py
    ::moduledescription: authentication validation admin
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib import admin

from authentication.models import Validation


class ValidationAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "key",
        "type",
        "is_active"
    )

    readonly_fields = [
        "key",
        "active_date"
    ]
    raw_id_fields = [
        "user"
    ]

admin.site.register(Validation, ValidationAdmin)
