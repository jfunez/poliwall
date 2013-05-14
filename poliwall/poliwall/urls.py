from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


from poliwall_api import v1_api


urlpatterns = patterns(
    '',
    # Initial pages
    url(r'^$', 'poliwall.views.home', name='home'),
    url(r'^gob-nacional/$', 'poliwall.views.gob_nacional', name='gob_nacional'),
    # Party
    url(r'^partidos/$', 'poliwall.views.party_list', name='party_list'),
    url(r'^partido/(?P<full_name>.+)/$', 'poliwall.views.party_detail', name='party_detail'),
    # Legislative
    url(r'^legislativo/$', 'poliwall.views.legislative_list', name='legislative_list'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/$', 'poliwall.views.legislative_detail', name='legislative_detail'),
    url(r'^legislativo/legislatura/(?P<legislative_code>\w+)/politicos/$', 'poliwall.views.legislative_politician_list', name='legislative_politician_list'),
    # Profile
    url(r'^perfil/(?P<slug>.+)/$', 'poliwall.views.legislative_politician_detail', name='legislative_politician_detail'),
    # Sessions
    url(r'^sesiones/$', 'poliwall.views.session_list', name='session_list'),
    url(r'^sesiones/legislatura/(?P<legislative_code>\w+)/$', 'poliwall.views.session_list', name='session_list_by_legis'),

    # Backend Tools
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
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
