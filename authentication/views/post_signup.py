# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.views post_signup.py
    ::moduledescription: post signup view
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib.auth import get_user_model
from django.http import HttpResponseNotFound
from django.views import View
from django.shortcuts import render

User = get_user_model()


class PostSignupView(View):
    """ post signup view """
    template_name = "authentication/post_signup.html"

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(
                uuid=kwargs.get("uuid")
            )
        except User.DoesNotExist:
            return HttpResponseNotFound()

        context = {
            "user": user
        }

        return render(request, self.template_name, context)
