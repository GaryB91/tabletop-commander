# -*- coding: UTF-8 -*-
"""
    ::module file: base - views.py
    ::module description: base app views
    ::module author: Gary Bullock <g.bullock91@gmail.com>
"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """ Home View """
    template_name = "base/home.html"
