from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


from poliwall_api import v1_api


urlpatterns = patterns(
    '',
    url(r'^$', 'poliwall.views.home', name='home'),
    # Gob. Nacional
    url(r'^gob-nacional/$', 'poliwall.views.gob_nacional', name='gob_nacional'),
    url(r'^poder-legislativo/politicos/$', 'poliwall.views.politician_list', name='politician_list'),
    url(r'^poder-legislativo/$', 'poliwall.views.poder_legislativo', name='poder_legislativo'),
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
