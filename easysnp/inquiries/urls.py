
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('inquiries.views',
        url(r'^inquiries/inquiries.html', 'inquiries'),
        url(r'^inquiries/inquiry.html', 'inquiry'),
        url(r'^inquiries/inquiry_edit.html', 'inquiry_edit')
)
