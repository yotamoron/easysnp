# Create your views here.

import main.ajax as ajax
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html',
        {
            'my_leads': ajax.load_url('/leads/my_leads.html'),
            'my_tasks': ajax.load_url('/tasks/my_tasks.html')
         })


