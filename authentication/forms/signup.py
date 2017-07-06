# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.forms signup.py
    ::moduledescription: authentication app signup form
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.ModelForm):
    """ signup model form """

    class Meta:
        model = User
        fields = [
            "email",
            "password"
        ]
