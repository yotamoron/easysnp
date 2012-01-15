
from django.conf.urls.defaults import patterns, include, url
from common.consts import UUID_PAT
from common.patterns import app_patterns

urlpatterns = app_patterns('leads.views', 'leads')
urlpatterns += patterns('leads.views',
        url(r'^leads/my_leads.html', 'my_leads'),
        url(r'^leads/leads.html', 'leads'))
