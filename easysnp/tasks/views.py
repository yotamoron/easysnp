# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def my_tasks(request):
    return render_to_response('my_tasks.html', {})

@login_required
def tasks(request):
    return render_to_response('tasks.html', {})

@login_required
def task(request):
    return render_to_response('task.html', {})
