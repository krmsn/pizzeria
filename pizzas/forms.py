from django import forms
from .models import Topping

class CommentForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name':''}
