# Create your views here.

from django.shortcuts import render_to_response

def settings(request):
    return render_to_response('settings.html', {})

