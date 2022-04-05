from django.forms import ModelForm
from django import forms
from .models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','name','mobile','password','is_admin']

