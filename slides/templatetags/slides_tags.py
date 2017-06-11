#
#   Copyright 2013, 2014
#             by Arnold Krille for bcs kommunikationsloesungen
#             <a.krille@b-c-s.de>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from django.template.loader import get_template
from django.template.context import Context

from mezzanine import template

from slides.models import Slide

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_homepage_slides(context, page=None):
    slides = Slide.objects.published()[:10]
    return slides