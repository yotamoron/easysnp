from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy

class AuthenticationRememberMeForm(AuthenticationForm):
    remember_me = forms.BooleanField(label=ugettext_lazy('Remember Me'),
            initial=False, required = False)
