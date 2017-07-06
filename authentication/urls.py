# -*- coding: UTF-8 -*-
"""
    ::module file: authentication urls.py
    ::moduledescription: authentication app urls
    ::moduleauthor: Gary Bullock <g.bullock91@gmail.com>
"""
from django.conf.urls import url

from authentication.views.login import LoginView
from authentication.views.signup import SignupView
from authentication.views.post_signup import PostSignupView
from authentication.views.password_reset_request import PasswordResetRequestView
from authentication.views.password_reset import PasswordResetView
from authentication.views.revalidation_request import RevalidationRequestView
from authentication.views.validation import ValidationView


urlpatterns = [
    url(
        regex='^signup/$',
        view=SignupView.as_view(),
        name='signup'
    ),
    url(
        regex='^login/$',
        view=LoginView.as_view(),
        name='login'
    ),
    url(
        regex='^post-signup/(?P<uuid>[-\w]+)/$',
        view=PostSignupView.as_view(),
        name='post-signup'
    ),
    url(
        regex='^password-reset-request/$',
        view=PasswordResetRequestView.as_view(),
        name='password-reset-request'
    ),
    url(
        regex='^password-reset/(?P<token>[-\w]+)/$',
        view=PasswordResetView.as_view(),
        name='password-reset'
    ),
    url(
        regex='^revalidation-request/$',
        view=RevalidationRequestView.as_view(),
        name='revalidation-request'
    ),
    url(
        regex='^validation/(?P<token>[-\w]+)/$',
        view=ValidationView.as_view(),
        name='validation'
    )
]
