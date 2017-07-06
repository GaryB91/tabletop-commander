# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.views revalidation_request.py
    ::moduledescription: revalidation request view
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.contrib.auth import get_user_model
from django.views.generic import FormView

from authentication.forms.email import EmailForm
from authentication.models.validation import Validation
from authentication.conf import settings
User = get_user_model()


class RevalidationRequestView(FormView):
    """Account revalidation request view"""
    template_name = "authentication/revalidation_request.html"
    form_class = EmailForm

    def form_valid(self, form):

        email = form.cleaned_data.get("email")
        context = self.get_context_data()

        try:
            user = User.objects.get(
                email=email
            )
            context.update({
                "user_exists": False,
                "is_sent": False,
                "is_not_validated": True
            })
        except User.DoesNotExist:
            pass
        else:

            if not user.is_validated:
                # disable any old validation instances
                old_requests = Validation.objects.filter(
                    user=user,
                    is_active=True,
                    type=Validation.ValidationType.ACCOUNT
                )
                old_requests.update(is_active=False)

                # create validation instance
                instance = Validation.objects.create(**{
                    "user": user,
                    "type": Validation.ValidationType.ACCOUNT,
                })
                # send email for password reset
                template_context = {"token": instance.key}
                template = MessageTemplate.objects.get(
                    pk=settings.SIGNUP_VALIDATION_TEMPLATE
                )
                user.send_system_email(template, template_context)
                context.update({
                    "user_exists": True,
                    "is_not_validated": True,
                    "is_sent": True
                })
            else:
                context.update({
                    "user_exists": True,
                    "is_not_validated": False,
                    "is_sent": False
                })

        return self.render_to_response(context)
