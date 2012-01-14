# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def contacts(request):
    return render_to_response('contacts.html', {})

@login_required
def contact(request):
    return render_to_response('contact.html', {})

@login_required
def contact_edit(request):
    return render_to_response('contact_edit.html', {})
