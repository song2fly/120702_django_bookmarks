#from django import newforms as forms
from django import forms

import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label='user name', max_length=30)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label = 'password', widget=forms.PasswordInput())
    password2 = forms.CharField(label = 'password_confirm', widget=forms.PasswordInput())
    
    #check password
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('not password')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('check username')
        
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('cannot user')
    
class BookmarkSaveForm(forms.Form):
    url = forms.URLField(
                         label='address',
                         widget=forms.TextInput(attrs={'size':64})
                         )
    title = forms.CharField(
                            label='title',
                            widget=forms.TextInput(attrs={'size':64})
                            )
    tags = forms.CharField(
                           label='TAG',
                           required=False,
                           widget=forms.TextInput(attrs={'size':64})
                           )
                


