
from django.conf.urls.defaults import patterns, url
from common.consts import UUID_PAT

def app_patterns(pat, app, view='view', edit='edit', delete='delete',
        new='new'):
    app_uuid = (app, UUID_PAT)
    return patterns(pat,
        url(r'^%s/view.html/(?P<oid>%s)/' % app_uuid, view),
        url(r'^%s/edit.html/(?P<oid>%s)/' % app_uuid, edit),
        url(r'^%s/delete.html/(?P<oid>%s)/' % app_uuid, delete),
        url(r'^%s/new.html' % app, new))
