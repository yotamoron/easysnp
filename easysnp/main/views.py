# Create your views here.

import main.ajax as ajax
from django.shortcuts import render_to_response

def index(request):
    panels = [ ajax.load_url('/leads/my_leads.html'),
               ajax.load_url('/tasks/my_tasks.html') ]
    return render_to_response('base.html',
            {'body': panels, 'title': 'Hello Kitty' })


