# -*- coding: utf-8 -*-
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from lockdown.decorators import lockdown
from polidata.models import LegislativePolitician
from polisessions.models import Action


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
def legislative_politician_list(request):
    senators_list = LegislativePolitician.objects.filter(house__name="Senadores")
    deputies_list = LegislativePolitician.objects.filter(house__name="Diputados")

    context = Context({
        'senators_list': senators_list,
        'deputies_list': deputies_list,
    })
    return render_to_response('legislative_politician_list.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_politician_detail(request, pk):
    legislative_politician = get_object_or_404(LegislativePolitician, pk=pk)
    legislative_politician_actions = Action.objects.filter(politician=legislative_politician.politician)

    context = Context({
        'legislative_politician': legislative_politician,
        'legislative_politician_actions': legislative_politician_actions,
    })
    return render_to_response('legislative_politician_detail.html', context, context_instance=RequestContext(request))
