#get generic user class
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    #password will be point point
    password = forms.CharField(widget=forms.PasswordInput)


    #Meta is information about your class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']