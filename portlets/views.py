# encoding: utf-8
import json

from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.http.response import HttpResponse


from .models import DialogPortlet

class DialogView(TemplateView):
    def get(self, request):
        success = False
        dialog_list = DialogPortlet.objects.published()
        try:
            dialog = dialog_list[0]
        except IndexError:
            html = ''
        else:
            context=RequestContext(request)
            html = dialog.render(context)
            success = html != None
            
        data = {
            'success': success,
            'html': html,
        }
        
        return HttpResponse(json.dumps(data))