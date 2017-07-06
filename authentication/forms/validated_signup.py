# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.forms validated_signup.py
    ::moduledescription: validated signup form
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from authentication.forms.signup import SignupForm


class ValidatedSignupForm(SignupForm):
    """ validated signup form """
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label=_("Confirm Password")
    )

    class Meta(SignupForm.Meta):
        """ ValidatedSignupForm meta"""
        fields = SignupForm.Meta.fields + ["confirm_password"]

    def clean_confirm_password(self):
        """ clean and validate password """

        value = self.cleaned_data.get("confirm_password")
        current_password = self.cleaned_data.get("password")
        if value != current_password:
            raise ValidationError(message=_("passwords do not match"))
        return value
