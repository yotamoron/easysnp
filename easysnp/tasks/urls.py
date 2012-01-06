
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tasks.views',
        url(r'^tasks/my_tasks.html', 'my_tasks')
    )
