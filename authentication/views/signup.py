# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.views signup.py
    ::moduledescription: authentication signup view
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import FormView

from authentication.conf import settings
from authentication.forms.validated_signup import ValidatedSignupForm
from authentication.models.validation import Validation


class SignupView(FormView):
    """ authentication signup view"""
    template_name = "authentication/signup.html"
    form_class = ValidatedSignupForm

    def form_valid(self, form):

        instance = form.save()
        validation = Validation.objects.create(**{
            "user": instance,
            "type": Validation.ValidationType.ACCOUNT,
        })
        # send email for password reset
        template_context = {"token": validation.key}
        # template = MessageTemplate.objects.get(
        #     pk=settings.PASSWORD_RESET_TEMPLATE
        # )
        # instance.send_system_email(template, template_context)
        return HttpResponseRedirect(
            redirect_to=reverse(
                viewname="authentication:post-signup",
                kwargs={
                    "uuid": instance.uuid
                }
            )
        )
