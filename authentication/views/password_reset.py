# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.views password_reset.py
    ::moduledescription: authentication app password reset
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib.auth import authenticate
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from authentication.forms.password_reset import PasswordResetForm
from authentication.models.validation import Validation


class PasswordResetView(View):
    """password reset view"""
    template_name = "authentication/password_reset.html"

    def get_form(self, request, *args, **kwargs):
        """get view form"""
        if request.method.lower() == "post":
            form = PasswordResetForm(
                data=request.POST
            )
        else:
            form = PasswordResetForm(
                initial={
                    "email": kwargs.get("email"),
                }
            )
        return form

    def get_validation_object(self, token):

        validation = None
        try:
            validation = Validation.objects.get(
                key=token,
                is_active=True
            )
        except Validation.DoesNotExist:
            pass
        return validation

    def get(self, request, *args, **kwargs):
        """get handler"""
        token = kwargs.get("token")
        validation = self.get_validation_object(token)
        if validation is None:
            return HttpResponseNotFound()

        form = self.get_form(
            request=request,
            email=validation.user.email
        )
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """post handler"""

        token = kwargs.get("token")
        validation = self.get_validation_object(token)
        form = self.get_form(request)
        reset_complete = False
        if form.is_valid():
            form_email = form.cleaned_data.get("email")
            old_password = form.cleaned_data.get("old_password")
            user = authenticate(
                email=form_email,
                password=old_password
            )
            if user is not None:
                user.set_password(
                    raw_password=form.cleaned_data("password")
                )
                user.is_validated = True
                user.save(update_fields=["password", "is_validated"])

                validation.is_active = False
                validation.active_date = timezone.now()
                validation.save(update_fields=["is_active, active_date"])
                reset_complete = True

        context = {
            "form": form,
            "is_reset_complete": reset_complete
        }
        return render(request, self.template_name, context)
