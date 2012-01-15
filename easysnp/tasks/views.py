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
def view(request, oid):
    return render_to_response('view_task.html', {})

@login_required
def edit(request, oid):
    return render_to_response('edit_task.html', {})

@login_required
def delete(request, oid):
    return render_to_response('delete_task.html', {})

@login_required
def new(request):
    return render_to_response('new_task.html', {})

