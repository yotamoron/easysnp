# Create your views here.

from django.contrib.auth.decorators import login_required
import main.ajax as ajax
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from urlparse import urlparse

def index(request):
    #if request.META.has_key('HTTP_REFERER'):
    #    referer = urlparse(request.META['HTTP_REFERER'])
    #    if referer.path == '/account/login/':
    #        query_args_list = referer.query.split('?')
    #        next_path = [arg for arg in query_args_list if arg.startswith('next')]
    #        if next_path:
    #            return HttpResponseRedirect(next_path[0].split('=')[1])

    panels = [ ajax.call('/leads/my_leads.html'),
               ajax.call('/tasks/my_tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

@login_required
def leads(request):
    panels = [ ajax.call('/leads/leads.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def lead(request):
    panels = [ ajax.call('/leads/lead.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })


def lead_edit(request):
    panels = [ ajax.call('/leads/lead_edit.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def settings(request):
    panels = [ ajax.call('/security/settings.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def contacts(request):
    panels = [ ajax.call('/contacts/contacts.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def contact(request):
    panels = [ ajax.call('/contacts/contact.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def tasks(request):
    panels = [ ajax.call('/tasks/tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def task(request):
    panels = [ ajax.call('/tasks/task.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def vessels(request):
    panels = [ ajax.call('/vessels/vessels.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def vessel(request):
    panels = [ ajax.call('/vessels/vessel.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def inquiries(request):
    panels = [ ajax.call('/inquiries/inquiries.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def inquiry(request):
    panels = [ ajax.call('/inquiries/inquiry.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
