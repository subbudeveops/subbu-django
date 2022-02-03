from email.policy import default
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

# Creating custom validator function 
def validat_email(value):
    if value[0].lower()!='s':
        raise ValidationError('message start should be S only')
    
class ContactForm(forms.Form):
    subject=forms.CharField(max_length=200,validators=[validators.MinLengthValidator(5)])
    message=forms.CharField(widget=forms.Textarea,validators=[validat_email]) #this is Django inbuilt validator 
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)