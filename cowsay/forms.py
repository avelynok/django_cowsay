from django import forms
from cowsay.models import Input

class InputForm(forms.Form):
    text = forms.CharField(max_length=150)