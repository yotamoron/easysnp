# Create your views here.

from django.contrib.auth.decorators import login_required
import main.ajax as ajax
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from urlparse import urlparse

@login_required
def index(request):
    panels = [ ajax.call('/leads/my_leads.html'),
               ajax.call('/tasks/my_tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'EasySnP' })

@login_required
def leads(request):
    panels = [ ajax.call('/leads/leads.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Leads' })

@login_required
def settings(request):
    panels = [ ajax.call('/security/settings.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Settings' })

@login_required
def contacts(request):
    panels = [ ajax.call('/contacts/contacts.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Contacts' })

@login_required
def tasks(request):
    panels = [ ajax.call('/tasks/tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Tasks' })

@login_required
def vessels(request):
    panels = [ ajax.call('/vessels/vessels.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Vessels' })

@login_required
def inquiries(request):
    panels = [ ajax.call('/inquiries/inquiries.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Inquiries' })

@login_required
def files(request):
    panels = [ ajax.call('/files/files.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Files' })

# The following functions handle the 4 basic actions that can
# be applied on an object: create a new object, edit an existing object,
# view an existing object, delete an existing object
@login_required
def view(request, app, oid):
    panels = [ ajax.call('/%s/view/%s/' % (app, oid)) ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def edit(request, app, oid):
    panels = [ ajax.call('/%s/edit/%s/' % (app, oid)) ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def delete(request, app, oid):
    panels = [ ajax.call('/%s/delete/%s/' % (app, oid)) ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def new(request, app):
    panels = [ ajax.call('/%s/new' % (app)) ]
    request.session['new_referer'] = request.get_full_path()
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
