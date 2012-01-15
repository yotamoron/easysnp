
from django.conf.urls.defaults import patterns, include, url
from common.consts import UUID_PAT
from common.patterns import app_patterns

urlpatterns = app_patterns('inquiries.views', 'inquiries')
urlpatterns += patterns('inquiries.views',
        url(r'^inquiries/inquiries.html', 'inquiries'))
