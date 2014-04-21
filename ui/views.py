from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def render_template(request):
    return render_to_response('base.html', RequestContext(request, {}))


def redirect_home(request):
    return redirect('/agiler/')