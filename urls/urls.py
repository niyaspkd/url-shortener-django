from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

short = '(?P<short>.{6})'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'manager.views.index'),
    url(r'^thanks/%s/$' % short, 'manager.views.thanks'),
    url(r'^%s$' % short, 'manager.views.activate'),
)
