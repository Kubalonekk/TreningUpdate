from django import forms
from django.forms import ModelForm
from .models import *



class ZakupForm(ModelForm):
    class Meta:
        model = Zakup