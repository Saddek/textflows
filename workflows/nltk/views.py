from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# modeli
from workflows.textflows_dot_net.serialization_utils import ToNetObj
from workflows.models import *
# auth fore
from django.contrib.auth.decorators import login_required

@login_required
def get_adc_index(request, widget_id, narrow_doc = 'n', document_id_from=0, document_id_to=-1):
    w = get_object_or_404(Widget, pk=widget_id)
    if w.workflow.user == request.user:
        firstInput = w.inputs.all()[0]
        #dc = ToNetObj(firstInput.value)
        #data = dc.MakeIndexPage(document_id_from, document_id_to, 100, narrow_doc)
        #data = "Roman"
        #return HttpResponse(data, mimetype='text/html')
        return HttpResponse()
    else:
        return HttpResponse(status=400)