# Create your views here.

from django.shortcuts import render_to_response

def contacts(request):
    return render_to_response('contacts.html', {})

def contact(request):
    return render_to_response('contact.html', {})

def contact_edit(request):
    return render_to_response('contact_edit.html', {})