# -*- coding: UTF-8 -*-
"""
    ::module file: authentication conf.py
    ::moduledescription: conf
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from base.utils import LazySettings

DEFAULT_SETTINGS = {
    "SIGNUP_REDIRECT_VIEW": "dashboard:dashboard",
    "SIGNUP_VALIDATION_TEMPLATE": 1,
    "PASSWORD_RESET_TEMPLATE": 2,
}


settings = LazySettings(DEFAULT_SETTINGS)
