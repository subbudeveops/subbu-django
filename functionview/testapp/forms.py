from django import forms
from .models import SubbuModel


class SubbuForm(forms.ModelForm):
    class Meta:
        model = SubbuModel
        fields = ['title', 'desc']
        #fields = "__all__"
        labels = {
            'title': 'TITLE',
            'desc': 'Description',
        }
