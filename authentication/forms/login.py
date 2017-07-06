# -*- coding: UTF-8 -*-
"""
    ::module file:  authentication.forms login.py
    ::moduledescription: authentication login form
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    """login form"""
    email = forms.EmailField(
        required=True,
        label=_("Email Address")
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label=_("Password")
    )
