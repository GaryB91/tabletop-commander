# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.forms password_reset.py
    ::moduledescription: authentication password reset form
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class PasswordResetForm(forms.Form):
    """ password reset form """
    email = forms.CharField(
        widget=forms.HiddenInput,
        required=True,
        label=_("Email Address")
    )

    old_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label=_("Old Password")
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label=_("Password")
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label=_("Confirm Password")
    )

    def clean_confirm_password(self):
        """ clean and validate password """
        value = self.cleaned_data.get("confirm_password")
        current_password = self.cleaned_data.get("password")

        if value != current_password:
            ValidationError(message=_("passwords do not match"))
        return value
