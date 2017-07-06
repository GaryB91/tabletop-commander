# -*- coding: UTF-8 -*-
"""
    ::module file: base urls.py
    ::module description: urls for base app
    ::module author: Gary Bullock <g.bullock91@gmail.com>
"""
from django.conf.urls import url

from base.views import HomeView

urlpatterns = [
    url('^$', view=HomeView.as_view(), name="home")
]
