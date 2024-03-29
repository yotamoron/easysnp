
from django.conf.urls.defaults import patterns, include, url
from common.consts import UUID_PAT

urlpatterns = patterns('main.views',
        url(r'^files.html', 'files'),
        url(r'^leads.html', 'leads'),
        url(r'^settings.html', 'settings'), # I think this should go away
        url(r'^contacts.html', 'contacts'),
        url(r'^tasks.html', 'tasks'),
        url(r'^vessels.html', 'vessels'),
        url(r'^inquiries.html', 'inquiries'),
        url(r'^edit/(?P<app>[a-z]+)/(?P<oid>%s)/' % UUID_PAT, 'edit'),
        url(r'^view/(?P<app>[a-z]+)/(?P<oid>%s)/' % UUID_PAT, 'view'),
        url(r'^delete/(?P<app>[a-z]+)/(?P<oid>%s)/' % UUID_PAT, 'delete'),
        url(r'^new/(?P<app>[a-z]+)/', 'new'),
        url(r'^index.html$', 'index')
    )
