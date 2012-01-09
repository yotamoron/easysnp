
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('contacts.views',
        url(r'^contacts/contacts.html', 'contacts'),
        url(r'^contacts/contact.html', 'contact'),
        url(r'^contacts/contact_edit.html', 'contact_edit')
)
