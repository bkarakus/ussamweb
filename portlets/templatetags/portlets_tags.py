# django imports
from django import template

from portlets.models import Portlet

register = template.Library()

@register.inclusion_tag('portlets/portlet_slot.html', takes_context=True)
def portlet_slot(context, slot):

    # Get portlets for given instance
    portlets = Portlet.objects.published().filter(slot=slot)

    rendered_portlets = []
    for portlet in portlets:
        try:
            portlet = portlet.get_content_model()
            rendered_portlets.append(portlet.render(context))
        except:
            pass

    return { "portlets" : rendered_portlets }