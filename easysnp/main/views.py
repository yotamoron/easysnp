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
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def leads(request):
    panels = [ ajax.call('/leads/leads.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def lead(request):
    panels = [ ajax.call('/leads/lead.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })


@login_required
def lead_edit(request):
    panels = [ ajax.call('/leads/lead_edit.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def settings(request):
    panels = [ ajax.call('/security/settings.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def contacts(request):
    panels = [ ajax.call('/contacts/contacts.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def contact(request):
    panels = [ ajax.call('/contacts/contact.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def tasks(request):
    panels = [ ajax.call('/tasks/tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def task(request):
    panels = [ ajax.call('/tasks/task.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def vessels(request):
    panels = [ ajax.call('/vessels/vessels.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def vessel(request):
    panels = [ ajax.call('/vessels/vessel.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def inquiries(request):
    panels = [ ajax.call('/inquiries/inquiries.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def inquiry(request):
    panels = [ ajax.call('/inquiries/inquiry.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
