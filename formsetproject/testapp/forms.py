from django import forms
class FormsetForm(forms.Form):
    name=forms.CharField(max_length=19)
    description=forms.CharField()

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('minimum character should be 4')
        return inputname
    def clean_des(self):
        inputdes=self.cleaned_data['description']
        if len(inputdes)<4:
            raise forms.ValidationError('minimum character should be 4')
        return inputdes



