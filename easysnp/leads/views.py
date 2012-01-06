# Create your views here.

from django.shortcuts import render_to_response

def my_leads(request):
    return render_to_response('my_leads.html', {})
