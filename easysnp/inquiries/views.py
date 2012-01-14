# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def inquiries(request):
    return render_to_response('inquiries.html', {})

@login_required
def inquiry(request):
    return render_to_response('inquiry.html', {})

@login_required
def inquiry_edit(request):
    return render_to_response('inquiry_edit.html', {})
