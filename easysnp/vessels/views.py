# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def vessels(request):
    return render_to_response('vessels.html', {})

@login_required
def vessel(request):
    return render_to_response('vessel.html', {})

@login_required
def vessel_edit(request):
    return render_to_response('vessel_edit.html', {})
