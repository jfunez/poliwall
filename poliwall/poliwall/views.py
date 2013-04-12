# -*- coding: utf-8 -*-
from django.template import Context, RequestContext
from django.shortcuts import render_to_response


def home(request):
    context = Context({
    })
    return render_to_response('home.html', context, context_instance=RequestContext(request))
