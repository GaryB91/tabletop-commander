# -*- coding: UTF-8 -*-
"""
    ::module file: base urls.py
    ::moduledescription: urls for base app
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.conf.urls import url

from base.views import HomeView

urlpatterns = [
    url('^$', view=HomeView.as_view(), name="home")
]
