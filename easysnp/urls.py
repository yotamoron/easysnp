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
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
)

for app in EXTRA_APPS:
        try:
            PRIO_APP = False
            mod = __import__("easysnp." + app + ".urls", globals(), locals(),
                    ['urlpatterns, PRIO_APP'], -1)
            try:
                PRIO_APP = mod.PRIO_APP
            except AttributeError:
                pass
            if PRIO_APP:
                urlpatterns = mod.urlpatterns + urlpatterns
            else:
                urlpatterns = urlpatterns + mod.urlpatterns
        except ImportError:
            # application doesn't have its own urls module - no worries.
            pass


