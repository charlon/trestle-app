from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

import urllib
import json

# create your views here

def example(request):
    return render_to_response('{{ app_name }}/example.html', context_instance=RequestContext(request))

def test(request):
    return render_to_response('{{ app_name }}/test.html', context_instance=RequestContext(request))
