from django.conf.urls.defaults import patterns, include, url

from easysnp.settings import EXTRA_APPS

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'easysnp.views.home', name='home'),
    # url(r'^easysnp/', include('easysnp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
)

for app in EXTRA_APPS:
        try:
            mod = __import__("easysnp." + app + ".urls", globals(), locals(),
                    ['urlpatterns'], -1)
            urlpatterns += mod.urlpatterns
        except ImportError:
            # application doesn't have its own urls module - no worries.
            pass


