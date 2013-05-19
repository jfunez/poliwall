# -*- coding: utf-8 -*-
from datetime import date
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
from lockdown.decorators import lockdown
from polidata.models import Politician, Legislative, House, Party
from polisessions.models import Session, Action
from polisalary.models import PoliticianSalary


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
    return render_to_response('national_gov.html', context, context_instance=RequestContext(request))


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
    if not parties.filter(name=full_name).exists():
        if parties.count() > 1:
            context = Context({
                'party_list': parties,
            })
            return render_to_response('party_list.html', context, context_instance=RequestContext(request))

    context = Context({
        'party': parties[0],
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
        'legislative_list': [legislative],
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
    latest_legislature = Legislative.objects.latest('code')
    politician_recent_activity = politician.actions.order_by('-session__date')[:10]

    context = Context({
        'politician': politician,
        'latest_legislature': latest_legislature,
        'politician_recent_activity': politician_recent_activity,
    })
    return render_to_response('legislative_politician_detail.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def session_list(request, legislative_code=None):
    house_sessions = []
    legislatives_code_set = set()
    legislative_year_set = set()
    legislatives = Legislative.objects.all()
    for legis in legislatives:
        legislatives_code_set.add(legis.roman_code)
        for year in xrange(legis.start_date.year, legis.end_date.year):
            legislative_year_set.add(year)

    year_filter = request.GET.get('year', None)
    try:
        year_filter = int(year_filter)
    except Exception:
        year_filter = None
    for house in House.objects.filter(is_public=True):
        sessions = Session.objects.filter(house=house)
        if year_filter:
            sessions = sessions.filter(date__year=year_filter)
        if legislative_code:
            legislative = get_legislative_by_code(legislative_code)
            sessions = sessions.filter(legislative=legislative)

        house_data = {
            'house_name': house.name,
            'sessions': sessions[0:20],
        }
        house_sessions.append(house_data)

    context = Context({
        'house_sessions': house_sessions,
        'legislatives_code_set': legislatives_code_set,
        'legislative_year_set': legislative_year_set
    })
    return render_to_response('session_list.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def action_list(request, legislative_code, session_pk):
    try:
        session = Session.objects.get(pk=session_pk)
        actions = Action.objects.filter(session__pk=session_pk)
    except Exception:
        raise Http404
    context = Context({
        'session': session,
        'actions': actions,
    })
    return render_to_response('action_list.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_salary_list(request, legislative_code):
    legislative = get_legislative_by_code(legislative_code)
    if not legislative:
        raise Http404
    salaries = PoliticianSalary.objects.filter(legislative=legislative).order_by('politician__last_name', 'politician__first_name')

    context = Context({
        'salaries': salaries,
        'legislative_code': legislative_code,
    })
    return render_to_response('salary_list.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_salary_detail(request, legislative_code, politician_slug):
    legislative = get_legislative_by_code(legislative_code)
    if not legislative:
        raise Http404

    politicians = Politician.objects.filter(slug__icontains=politician_slug)
    if not politicians.exists():
        raise Http404

    salaries = dict()
    for politician in politicians:
        salaries[politician.pk] = PoliticianSalary.objects.filter(
                                    legislative=legislative, politician__pk=politician.pk).order_by(
                                    'politician__last_name', 'politician__first_name', 'start_date')
    context = Context({
        'politicians': politicians,
        'salaries': salaries,
        'politician_slug': politician_slug,
        'legislative_code': legislative_code,
    })
    return render_to_response('salary_detail.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_statistics(request, legislative_code):
    legislative = get_legislative_by_code(legislative_code)
    if not legislative:
        raise Http404
    context = Context({
        'legislative_list': [legislative,]
    })
    return render_to_response('legislative_statistics.html', context, context_instance=RequestContext(request))


@lockdown(superusers_only=True)
def legislative_statistics_report(request, legislative_code, report_slug):
    legislative = get_legislative_by_code(legislative_code)
    if not legislative:
        raise Http404
    from model_report.report import reports
    report_class = reports.get_report(report_slug)
    if not report_class:
        raise Http404

    class FilteredReport(report_class):

        def get_legislative(self):
            return legislative

        def filter_query(self, qs):
            qs = qs.filter(legislative=legislative)
            return qs

    report = FilteredReport(request=request)

    return report.render(request, extra_context={'legislative': legislative})

