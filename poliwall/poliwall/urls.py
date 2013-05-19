from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from model_report import report
report.autodiscover()

from poliwall_api import v1_api


urlpatterns = patterns(
    '',
    # Initial pages
    url(r'^$', 'poliwall.views.home', name='home'),
    url(r'^acerca_de_polidatosuy/$', 'poliwall.views.about', name='about'),
    url(r'^gob-nacional/$', 'poliwall.views.gob_nacional', name='gob_nacional'),
    # Party
    url(r'^partidos/$', 'poliwall.views.party_list', name='party_list'),
    url(r'^partido/(?P<full_name>.+)/$', 'poliwall.views.party_detail', name='party_detail'),
    # Legislative
    url(r'^legislativo/$', 'poliwall.views.legislative_list', name='legislative_list'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/$', 'poliwall.views.legislative_detail', name='legislative_detail'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/politicos/$', 'poliwall.views.legislative_politician_list', name='legislative_politician_list'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/estadisticas/$', 'poliwall.views.legislative_statistics', name='legislative_statistics'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/estadisticas/(?P<report_slug>\w+)/$', 'poliwall.views.legislative_statistics_report', name='legislative_statistics_report'),
    # Profile
    url(r'^perfil/(?P<slug>.+)/$', 'poliwall.views.legislative_politician_detail', name='legislative_politician_detail'),
    # Actions
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/sesiones/(?P<session_pk>\w+)/actuaciones/$', 'poliwall.views.action_list', name='action_list_of_session'),
    # Sessions
    url(r'^legislativo/sesiones/$', 'poliwall.views.session_list', name='session_list'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/sesiones/$', 'poliwall.views.session_list', name='session_list_by_legis'),
    # Salary
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/remuneraciones/$', 'poliwall.views.legislative_salary_list', name='salary_list_by_legis'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/politicos/(?P<politician_slug>.+)/remuneraciones/$', 'poliwall.views.legislative_salary_detail', name='salary_detail_by_legis'),
    # Backend Tools
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^reportes/', include('model_report.urls')),
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^rosetta/', include('rosetta.urls')),
    )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$',  'serve', {'document_root': settings.MEDIA_ROOT}),
    )
