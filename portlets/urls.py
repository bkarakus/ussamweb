from __future__ import absolute_import

from django.conf.urls import patterns, url
from django.views.decorators.cache import never_cache
from . import views

urlpatterns = patterns('',
    url(regex = r'^get-dialog$',
        view  = (never_cache)(views.DialogView.as_view()),
        name  = 'get_dialog',
    ),
)