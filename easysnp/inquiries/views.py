# Create your views here.

from django.shortcuts import render_to_response

def inquiries(request):
    return render_to_response('inquiries.html', {})

def inquiry(request):
    return render_to_response('inquiry.html', {})

def inquiry_edit(request):
    return render_to_response('inquiry_edit.html', {})