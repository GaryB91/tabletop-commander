# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.forms email.py
    ::moduledescription: authentication app email form
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django import forms
from django.utils.translation import ugettext_lazy as _


class EmailForm(forms.Form):
    """email form"""
    email = forms.EmailField(
        required=True,
        label=_("Email Address")
    )
