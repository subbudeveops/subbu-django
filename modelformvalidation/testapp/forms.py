from django import forms
from django.forms import fields, widgets
from .models import Post
from .models import ValidModel
from .models import MovieModel


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"
       
        
    # form validation
    def clean(self):
        super(PostForm,self).clean()
        username=self.cleaned_data.get('username')
        text=self.cleaned_data.get('text')
        if len(username)<4:
            self._errors['username']=self.error_class(['minimum  characters required'])
        if len(text)<4:
            self._errors['text'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])
        
        return self.cleaned_data
    
class ValidForm(forms.ModelForm):
    class Meta:
        model=ValidModel
        fields='__all__'
    
    
class MovieForm(forms.ModelForm):
    class Meta:

        model=MovieModel
        fields=("movie_name","relase_date","hero_name","heroine_name","director_name","movie_name")
        labels={
            "movie_name":'Movie Name',
            "relase_date":'Relesing Date',
            "hero_name":'HeroName',
            "heroine_name":"Heroine Name",
            "director_name":'Director Name',

        }
        
        widgets={
            'movie_name':forms.TextInput(attrs={'class':'form-control','placeholder':'MovieName'}),
            'relase_date':forms.SelectDateWidget(attrs={'class':'form-control','placeholder':'Date Formoat YYYY-MM-DD'}),
            'hero_name':forms.TextInput(attrs={'class':'form-control','placeholder':' HeroName'}),
            'heroine_name':forms.TextInput(attrs={'class':'form-control','placeholder':'HeroineName '}),
            'director_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Director Name'}),


            }

        # form validation we create method
    def clean(self):

        super(MovieForm,self).clean()

        movie_name=self.cleaned_data.get('movie_name')
        if len(movie_name)<2:
            self._errors['movie_name']=self.error_class(['Movie Name should at leat 2 characters'])
        hero_name=self.cleaned_data.get('hero_name')
        if len(hero_name)<2:
            self._errors['hero_name']=self.error_class(['Hero Name should at leat 2 characters'])
        return self.cleaned_data
        heroine_name=self.cleaned_data.get('heroine_name')
        if len(heroine_name)<2:
            self._errors['heroine_name']=self.error_class(['Heroine Name at least 2 Character'])