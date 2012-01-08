
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('security.views',
        url(r'^security/login.html', 'login')
)
