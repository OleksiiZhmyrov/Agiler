from django.shortcuts import render_to_response
from django.template import RequestContext


def render_template(request):
    return render_to_response('skeleton/base.html', RequestContext(request, {}))