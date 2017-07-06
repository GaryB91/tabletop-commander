# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.models validation.py
    ::moduledescription: authentication app validation model
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Validation(models.Model):
    """
    validation model for authentication based requests
    """
    class ValidationType(object):
        """ validation type """
        ACCOUNT = 10
        PASSWORD = 20

        choices = (
            (ACCOUNT, _("Account Validation")),
            (PASSWORD, _("Password Validation"))
        )

    key = models.UUIDField(
        verbose_name=_("Validation key"),
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    user = models.ForeignKey(
        to=User,
        verbose_name=_("User")
    )

    type = models.IntegerField(
        verbose_name=_("Validation Type"),
        choices=ValidationType.choices,
        default=ValidationType.ACCOUNT
    )

    date = models.DateTimeField(
        default=timezone.now
    )

    active_date = models.DateTimeField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("active")
    )
