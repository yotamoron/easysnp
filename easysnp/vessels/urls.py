
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('vessels.views',
        url(r'^vessels/vessels.html', 'vessels'),
        url(r'^vessels/vessel.html', 'vessel'),
        url(r'^vessels/vessel_edit.html', 'vessel_edit')
)
