
from django.conf.urls.defaults import patterns, include, url
from common.consts import UUID_PAT
from common.patterns import app_patterns

urlpatterns = app_patterns('tasks.views', 'tasks')
urlpatterns += patterns('tasks.views',
        url(r'^tasks/my_tasks.html', 'my_tasks'),
        url(r'^tasks/tasks.html', 'tasks'))
