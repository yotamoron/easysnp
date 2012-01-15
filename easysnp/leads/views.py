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
def view(request, oid):
    return render_to_response('view_lead.html', {})

@login_required
def edit(request, oid):
    return render_to_response('edit_lead.html', {})

@login_required
def delete(request, oid):
    return render_to_response('delete_lead.html', {})

@login_required
def new(request):
    return render_to_response('new_lead.html', {})

