
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
        url(r'^leads.html', 'leads'),
        url(r'^lead.html', 'lead'),
        url(r'^lead_edit.html', 'lead_edit'),
        url(r'^login.html', 'login'),
        url(r'^', 'index')
    )
