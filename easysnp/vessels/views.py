# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def vessels(request):
    return render_to_response('vessels.html', {})

@login_required
def view(request, oid):
    return render_to_response('view_vessel.html', {})

@login_required
def edit(request, oid):
    return render_to_response('edit_vessel.html', {})

@login_required
def delete(request, oid):
    return render_to_response('delete_vessel.html', {})

@login_required
def new(request):
    return render_to_response('new_vessel.html', {})

