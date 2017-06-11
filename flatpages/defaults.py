from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting

register_setting(
    name="FLATPAGE_PER_PAGE",
    label=_("Blog posts per page"),
    description=_("Number of blog posts shown on a blog listing page."),
    editable=True,
    default=5,
)