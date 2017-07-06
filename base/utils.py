# -*- coding: UTF-8 -*-
"""
    ::module file: base utils.py
    ::moduledescription: base projet utilities
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.conf import settings as base_settings


class LazySettings(object):
    """Lazy Settings object"""
    def __init__(self, default):
        self.settings = default

    def __getattr__(self, item):
        try:
            value = self.settings[item]
        except KeyError:
            value = getattr(base_settings, item, None)

        if value is None:
            raise AttributeError
        return value
