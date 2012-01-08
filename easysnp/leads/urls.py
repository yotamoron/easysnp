
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('leads.views',
        url(r'^leads/my_leads.html', 'my_leads'),
        url(r'^leads/leads.html', 'leads'),
        url(r'^leads/lead.html', 'lead'),
        url(r'^leads/lead_edit.html', 'lead_edit')
)
