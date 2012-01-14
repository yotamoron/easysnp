# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def my_leads(request):
    return render_to_response('my_leads.html', {})

@login_required
def leads(request):
    return render_to_response('leads.html', {})

@login_required
def lead(request):
    return render_to_response('lead.html', {})

@login_required
def lead_edit(request):
    return render_to_response('lead_edit.html', {})
