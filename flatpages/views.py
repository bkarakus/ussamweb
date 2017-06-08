from __future__ import unicode_literals
from future.builtins import str, int

from calendar import month_name

from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import paginate

from flatpages.models import FlatPage, FlatPageCategory

User = get_user_model()


def flatpage_list(request, tag=None, username=None,
                   category=None, template="flatpages/flatpage_list.html",
                   extra_context=None):
    """
    Display a list of blog posts that are filtered by tag, year, month,
    author or category. Custom templates are checked for using the name
    ``blog/blog_post_list_XXX.html`` where ``XXX`` is either the
    category slug or author's username if given.
    """
    templates = []
    flatpages_qs = FlatPage.objects.published(for_user=request.user)
    if tag is not None:
        tag = get_object_or_404(Keyword, slug=tag)
        flatpages_qs = flatpages_qs.filter(keywords__keyword=tag)
    
    if category is not None:
        category = get_object_or_404(FlatPageCategory, slug=category)
        flatpages_qs = flatpages_qs.filter(categories=category)
        templates.append(u"flatpages_qs/flatpage_list_%s.html" %
                          str(category.slug))
    author = None
    if username is not None:
        author = get_object_or_404(User, username=username)
        flatpages_qs = flatpages_qs.filter(user=author)
        templates.append(u"flatpages_qs/flatpage_list_%s.html" % username)

    prefetch = ("categories", "keywords__keyword")
    flatpages_qs = flatpages_qs.select_related("user").prefetch_related(*prefetch)
    flatpages_qs = paginate(flatpages_qs, request.GET.get("page", 1),
                          settings.FLATPAGE_PER_PAGE,
                          settings.MAX_PAGING_LINKS)
    context = {"flatpages_qs": flatpages_qs,
               "tag": tag, "category": category, "author": author}
    context.update(extra_context or {})
    templates.append(template)
    return TemplateResponse(request, templates, context)


def flatpage_detail(request, slug,
                     template="flatpages/flatpage_detail.html",
                     extra_context=None):
    """. Custom templates are checked for using the name
    ``blog/blog_post_detail_XXX.html`` where ``XXX`` is the blog
    posts's slug.
    """
    flatpages_qs = FlatPage.objects.published(
                                     for_user=request.user).select_related()
    flatpage = get_object_or_404(flatpages_qs, slug=slug)
    
    context = {"flatpage": flatpage, "editable_obj": flatpage,}
    context.update(extra_context or {})
    templates = [u"flatpages/flatpage_detail_%s.html" % str(slug), template]
    return TemplateResponse(request, templates, context)