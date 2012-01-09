# Create your views here.

import main.ajax as ajax
from django.shortcuts import render_to_response

def index(request):
    panels = [ ajax.load_url('/leads/my_leads.html'),
               ajax.load_url('/tasks/my_tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def leads(request):
    panels = [ ajax.load_url('/leads/leads.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def lead(request):
    panels = [ ajax.load_url('/leads/lead.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })


def lead_edit(request):
    panels = [ ajax.load_url('/leads/lead_edit.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def login(request):
    panels = [ ajax.load_url('/security/login.html') ]
    return render_to_response('base_menuless.html',
            {'body': panels, 'title': 'Hello Kitty' })
    
def settings(request):
    panels = [ ajax.load_url('/security/settings.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
    
def contacts(request):
    panels = [ ajax.load_url('/contacts/contacts.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
    
def contact(request):
    panels = [ ajax.load_url('/contacts/contact.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
    
def tasks(request):
    panels = [ ajax.load_url('/tasks/tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def task(request):
    panels = [ ajax.load_url('/tasks/task.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def vessels(request):
    panels = [ ajax.load_url('/vessels/vessels.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
    
def vessel(request):
    panels = [ ajax.load_url('/vessels/vessel.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })

def inquiries(request):
    panels = [ ajax.load_url('/inquiries/inquiries.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
    
def inquiry(request):
    panels = [ ajax.load_url('/inquiries/inquiry.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })
