
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
        url(r'^leads.html', 'leads'),
        url(r'^lead.html', 'lead'),
        url(r'^lead_edit.html', 'lead_edit'),
        url(r'^login.html', 'login'),
        url(r'^settings.html', 'settings'),
        url(r'^contacts.html', 'contacts'),
        url(r'^contact.html', 'contact'),
        url(r'^tasks.html', 'tasks'),
        url(r'^task.html', 'task'),
        url(r'^', 'index')
    )
