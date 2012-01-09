# Create your views here.

from django.shortcuts import render_to_response

def vessels(request):
    return render_to_response('vessels.html', {})

def vessel(request):
    return render_to_response('vessel.html', {})

def vessel_edit(request):
    return render_to_response('vessel_edit.html', {})