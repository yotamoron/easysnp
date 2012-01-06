# Create your views here.

from django.shortcuts import render_to_response

def my_tasks(request):
    return render_to_response('my_tasks.html', {})
