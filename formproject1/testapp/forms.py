from email.policy import default
from django import forms
from django.core import validators
import datetime
class BasicForm(forms.Form):
  name=forms.CharField(max_length=15)
  date=forms.SelectDateWidget()
  email=forms.EmailField(help_text="ex@gmail.com",error_messages={'required':'Please Enter the correct Email id and password'})
  feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])

  def clean_name(self):
    total_cleaned_data=super().clean()
    inputname=total_cleaned_data['name']
    if len(inputname)<4:
      raise forms.ValidationError('the character should be at least 4 ')
    return inputname




    

class HiddenForm(forms.Form):
  name=forms.CharField(max_length=20)
  password=forms.HiddenInput()



