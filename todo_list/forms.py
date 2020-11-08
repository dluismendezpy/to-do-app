# Django
from django import forms

# Owns
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
