# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.views password_reset_request.py
    ::moduledescription: authentication password reset request
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib.auth import get_user_model
from django.views.generic import FormView

from authentication.conf import settings
from authentication.forms.email import EmailForm
from authentication.models.validation import Validation

User = get_user_model()


class PasswordResetRequestView(FormView):
    """password reset request view"""
    template_name = "authentication/password_reset_request.html"
    form_class = EmailForm

    def form_valid(self, form):

        email = form.cleaned_data.get("email")
        context = self.get_context_data()
        try:
            user = User.objects.get(
                email=email
            )
        except User.DoesNotExist:
            context.update({
                "user_exists": False,
                "is_validated": False,
                "is_sent": False
            })
        else:
            if user.is_validated:
                # disable any old validation instances
                old_requests = Validation.objects.filter(
                    user=user,
                    is_active=True,
                    type=Validation.ValidationType.PASSWORD
                )
                old_requests.update(is_active=False)

                # create validation instance
                instance = Validation.objects.create(**{
                    "user": user,
                    "type": Validation.ValidationType.PASSWORD,
                })
                # send email for password reset
                template_context = {"token": instance.key}
                template = MessageTemplate.objects.get(
                  pk=settings.PASSWORD_RESET_TEMPLATE
                )
                user.send_system_email(template, template_context)
                context.update({
                    "is_sent": True
                })

            context.update({
                "user_exists": True,
                "is_validated": user.is_validated
            })

        return self.render_to_response(context)
