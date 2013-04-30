# -*- coding: utf-8 -*-
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
from lockdown.decorators import lockdown
from polidata.models import Politician, Legislative, House, Party


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
def party_list(request):
    context = Context({
        'party_list': Party.objects.all()
    })
    return render_to_response('party_list.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def party_detail(request, full_name):
    parties = Party.objects.filter(name__icontains=full_name)
    if not parties.exists():
        raise Http404
    if parties.count() > 1:
        context = Context({
            'party_list': parties,
        })
        return render_to_response('party_list.html', context, context_instance=RequestContext(request))
    context = Context({
        'party': parties[0]
    })
    return render_to_response('party_detail.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_list(request):
    context = Context({
        'legislative_list': Legislative.objects.all().order_by('-start_date')
    })
    return render_to_response('legislative_list.html', context, context_instance=RequestContext(request))


def get_legislative_by_code(legislative_code):
    try:
        return Legislative.objects.get(code=int(legislative_code))
    except:
        try:
            return Legislative.objects.get(roman_code=legislative_code.upper())
        except:
            pass
    return None


@lockdown(superusers_only=True)
def legislative_detail(request, legislative_code):
    legislative = get_legislative_by_code(legislative_code)
    if not legislative:
        raise Http404

    context = Context({
        'legislative_list': [legislative]
    })
    return render_to_response('legislative_list.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_politician_list(request, legislative_code):
    legislative = get_legislative_by_code(legislative_code)
    if not legislative:
        raise Http404

    houses = []
    for house in House.objects.filter(is_public=True):
        qs = house.ligislativepolitician_houses.all()
        qs = qs.filter(legislative=legislative)
        legislative_list = list(qs.prefetch_related())
        if legislative_list:
            houses.append([house, legislative_list])
    context = Context({
        'houses': houses,
        'legislative': legislative,
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
