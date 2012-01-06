
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('leads.views',
        url(r'^leads/my_leads.html', 'my_leads')
    )
