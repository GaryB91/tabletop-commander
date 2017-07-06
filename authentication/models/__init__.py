# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.models __init__.py
    ::moduledescription: authentication models
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from authentication.models.user import User
from authentication.models.validation import Validation

__all__ = [
    "User",
    "Validation"
]
