# -*- coding: utf-8 -*-
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
from lockdown.decorators import lockdown
from polidata.models import LegislativePolitician, Politician, Legislative


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
def legislative_politician_list(request, legislative=None):
    legislatives = LegislativePolitician.objects.all()
    if legislative:
        if not Legislative.objects.filter(code=legislative).exists():
            raise Http404
        legislatives = legislatives.filter(legislative__code=legislative)
    senators_list = legislatives.filter(house__name="Senadores")
    deputies_list = legislatives.filter(house__name="Diputados")

    context = Context({
        'senators_list': senators_list,
        'deputies_list': deputies_list,
    })
    return render_to_response('legislative_politician_list.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_politician_detail(request, slug):
    politicians = Politician.objects.filter(slug__icontains=slug)
    if not politicians.exists():
        raise Http404
    if politicians.count() > 1:
        context = Context({
            'politician_list': politicians,
        })
        return render_to_response('politician_list.html', context, context_instance=RequestContext(request))
    politician = politicians[0]

    context = Context({
        'politician': politician,
    })
    return render_to_response('legislative_politician_detail.html', context, context_instance=RequestContext(request))
