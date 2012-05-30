# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()
    referrer = forms.CharField()

@login_required
def files(request):
    return render_to_response('files.html', {})

@login_required
def view(request, oid):
    return render_to_response('view_file.html', {})

@login_required
def edit(request, oid):
    return render_to_response('edit_file.html', {})

@login_required
def delete(request, oid):
    return render_to_response('delete_file.html', {})

@login_required
def new(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(request.session['new_referer'])
    else:
        form = UploadFileForm()
    return render_to_response('new_file.html', {'form': form},
            RequestContext(request))

