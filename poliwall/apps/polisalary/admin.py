# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls.defaults import patterns, url
from django.utils.encoding import force_unicode
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from polisalary.models import PoliticianSalary
from polisalary.forms import SetSalaryForm


class PoliticianSalaryAdmin(admin.ModelAdmin):
    list_display = ('politician', 'start_date', 'end_date', 'amount')
    list_filter = ('start_date',)
    search_fields = ('politician__first_name', 'politician__last_name')

    def get_urls(self):
        urls = super(PoliticianSalaryAdmin, self).get_urls()
        urls = patterns('',
                        url(r'^ingresar-sueldo/$', self.admin_site.admin_view(
                            self.admin_set_salary)),
                        ) + urls
        return urls

    def admin_set_salary(self, request, template_name='admin/polisalary/politiciansalary/admin_set_salary.html'):
        form = SetSalaryForm(request.POST or None)
        results = {}
        if form.is_valid():
            results = form.save()
            results['has_results'] = True

        context = {
            'form': form
        }
        opts = PoliticianSalary._meta
        admin_context = {
            'opts': opts,
            'app_label': opts.app_label,
            'title': _(u'Ingresar sueldo'),
            'object_name': force_unicode(opts.verbose_name),
        }
        context.update(admin_context)
        context.update(results)
        return render_to_response(template_name, context, RequestContext(request))


admin.site.register(PoliticianSalary, PoliticianSalaryAdmin)
