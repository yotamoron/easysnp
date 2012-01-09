
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
        url(r'^leads.html', 'leads'),
        url(r'^lead.html', 'lead'),
        url(r'^lead_edit.html', 'lead_edit'),
        url(r'^settings.html', 'settings'),
        url(r'^contacts.html', 'contacts'),
        url(r'^contact.html', 'contact'),
        url(r'^tasks.html', 'tasks'),
        url(r'^task.html', 'task'),
        url(r'^vessels.html', 'vessels'),
        url(r'^vessel.html', 'vessel'),
        url(r'^inquiries.html', 'inquiries'),
        url(r'^inquiry.html', 'inquiry'),
        url(r'^', 'index')
    )
