
from django.conf.urls.defaults import patterns, include, url
from common.consts import UUID_PAT
from common.patterns import app_patterns

urlpatterns = app_patterns('contacts.views', 'contacts')
urlpatterns += patterns('contacts.views',
        url(r'^contacts/contacts.html', 'contacts'))
