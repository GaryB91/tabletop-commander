# -*- coding: UTF-8 -*-
"""
    ::module file: authentication.models user.py
    ::moduledescription: user model
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
import uuid as uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.template import Template, Context
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from authentication.managers.user import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ User model """

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_('uuid')
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        db_index=True
    )
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
        blank=True
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_validated = models.BooleanField(
        _('validated'),
        default=False,
        help_text=_(
            'Designates whether this user has passed account validation.'
        ),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        """User meta"""
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return "{first} {last}".format(
            first=self.first_name,
            last=self.last_name
        )

    def get_short_name(self):
        return self.first_name

    def send_system_email(self, template, context):

        t = Template(template_string=template.content)
        ctx = Context(context)
        content = t.render(ctx)

        # send_email(
        #     to=[self.email],
        #     from=settings.SYSTEM_EMAIL_ADDRESS,
        #     subject=template.subject,
        #     html=content
        # )
