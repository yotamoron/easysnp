
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('security.views',
        url(r'^security/settings.html', 'settings'),
        url(r'^accounts/login/', 'remember_me_login'),
)

PRIO_APP = True
