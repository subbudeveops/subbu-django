from django import forms 
from .models import SubbuModel
class SubbuForm(forms.ModelForm):
    class Meta:
        model=SubbuModel
        fields="__all__"
        fields=('name','subbu_field','marrage_image','subbu_file','uplaod_date','updated_date')
        
    def clean(self):
        super(SubbuForm,self).clean()
        name=self.cleaned_data.get('name')
        subbu_field=self.cleaned_data.get('subbu_field')

        if len(name)<4:
            self._errors['name']=self.error_class([ 'Minimum 5 characters required'])
        if len(subbu_field)<10:
            self._errors['subbu_field']=self.error_class([ 'Minimum 10 characters required'])
        return self.cleaned_data
        
            
               
                
               
            