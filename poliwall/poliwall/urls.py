from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'poliwall.views.home', name='home'),
    # url(r'^poliwall/', include('poliwall.foo.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
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
