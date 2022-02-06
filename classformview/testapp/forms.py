from turtle import title
from django import forms
from django .core.exceptions import ValidationError
class SubbuForm(forms.Form):
    title=forms.CharField(max_length=20)
    description = forms.CharField(widget = forms.Textarea)
    
    #validation 
    def form_valid(self,form):
        
        print(form.cleaned_data)
        return super.form_valid(form)
            
    