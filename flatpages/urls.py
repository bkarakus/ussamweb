from __future__ import unicode_literals

from django.conf.urls import url

from . import views
from mezzanine.conf import settings


# Trailing slahes for urlpatterns based on setup.
_slash = "/" if settings.APPEND_SLASH else ""

# Blog patterns.
urlpatterns = [
    url("^tag/(?P<tag>.*)%s$" % _slash,
        views.flatpage_list, name="flatpage_list_tag"),
    url("^category/(?P<category>.*)%s$" % _slash,
        views.flatpage_list, name="flatpage_list_category"),
    url("^author/(?P<username>.*)%s$" % _slash,
        views.flatpage_list, name="flatpage_list_author"),
    url("^(?P<slug>.*)%s$" % _slash,
        views.flatpage_detail, name="flatpage_detail"),
    url("^$", views.flatpage_list, name="flatpage_list"),
]