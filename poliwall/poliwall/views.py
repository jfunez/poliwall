# -*- coding: utf-8 -*-
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

from lockdown.decorators import lockdown

from polidata.models import Politician


@lockdown(superusers_only=True)
def home(request):
    context = Context({
    })
    return render_to_response('home.html', context, context_instance=RequestContext(request))


def api_home(request):
    context = Context({
    })
    return render_to_response('tastypie7home.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def gob_nacional(request):
    context = Context({
    })
    return render_to_response('gob_nacional.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def poder_legislativo(request):
    context = Context({
    })
    return render_to_response('poder_legislativo.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def politician_list(request):
    politicians = Politician.objects.all()
    context = Context({
        'politicians': politicians,
    })
    return render_to_response('politician_list.html', context, context_instance=RequestContext(request))
