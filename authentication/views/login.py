# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.views login.py
    ::moduledescription: authentication app login view
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import (
    render,
    reverse
)

from authentication.forms.login import LoginForm


class LoginView(View):
    """login form"""
    template_name = "authentication/login.html"
    form_class = LoginForm

    def get_form(self, request, *args, **kwargs):
        """ return view form class """
        form = self.form_class(
            data=request.POST
            if request.method.lower() == "post"
            else None
        )
        return form

    def get(self, request, *args, **kwargs):
        """ get handler """
        form = self.get_form(request, *args, **kwargs)
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.get_form(request, *args, **kwargs)
        context = {
            "form": form,
            "validation_required": False
        }

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request=request,
                email=email,
                password=password
            )

            if user is not None:
                if user.is_validated:
                    login(
                        request=request,
                        user=user
                    )
                    return HttpResponseRedirect(
                        redirect_to=reverse(
                            viewname="base:home"
                        )
                    )
                elif not user.is_validated:
                    context.update({
                        "validation_required": True
                    })
        return render(request, self.template_name, context)
