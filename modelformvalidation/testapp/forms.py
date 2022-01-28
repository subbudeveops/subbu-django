from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"
    def clean(self):
        super(PostForm,self).clean()
        username=self.cleaned_data.get['username']
        text=self.cleaned_data.get('text')
        if len(username)<4:
            self._errors['username']+errself.error_class(['minimum  characters required'])
        if len(text)<4:
            raise val