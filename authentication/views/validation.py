# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.views validation.py
    ::moduledescription:
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from authentication.models.validation import Validation


class ValidationView(View):
    """validation view"""
    template_name = "authentication/validation.html"

    def get(self, request, *args, **kwargs):

        token = kwargs.get("token")
        if token is None:
            return HttpResponseNotFound()

        try:
            validation = Validation.objects.get(
                key=token,
                is_active=True
            )
        except Validation.DoesNotExist:
            return HttpResponseNotFound()

        validation.user.is_validated = True
        validation.user.save(update_fields=["is_validated"])

        validation.is_active = False
        validation.active_date = timezone.now()
        validation.save(update_fields=["is_active, active_date"])

        return render(request, self.template_name, {})