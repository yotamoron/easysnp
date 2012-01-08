# Create your views here.

from django.shortcuts import render_to_response

def my_leads(request):
    return render_to_response('my_leads.html', {})

def leads(request):
    return render_to_response('leads.html', {})

def lead(request):
    return render_to_response('lead.html', {})

