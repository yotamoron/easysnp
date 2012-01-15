
from django.conf.urls.defaults import patterns, include, url
from common.consts import UUID_PAT
from common.patterns import app_patterns

urlpatterns = app_patterns('vessels.views', 'vessels')
urlpatterns += patterns('vessels.views',
        url(r'^vessels/vessels.html', 'vessels'))
