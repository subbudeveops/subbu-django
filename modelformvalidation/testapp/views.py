from django.shortcuts import render
from .forms import PostForm, ValidForm,MovieForm
from django.http import HttpResponse
from .models import Post,MovieModel
# Create your views here.
def model_form_view(request):
    
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
           
            return HttpResponse('<h3 style="center"> form submitted sucessfully</h3>')
        else:
            return render(request, "testapp/modelformvalidation.html", {'form':form}) 
    else:
        
        form=PostForm(None)
        return render(request,'testapp/modelformvalidation.html',{'form':form})
    
    
    
    
def list_model_form_view(request):
    model_list=Post.objects.all()
    return render(request,"testapp/listmodelform.html",{'model_list':model_list})


def gmail_valid_view(request):
    if request.method=='POST':
        form = ValidForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3 style="center"> form submitted sucessfully</h3>')
        else:
            return render(request, "testapp/modelformvalidation1.html", {'form':form}) 
    else:
        
        form=ValidForm(None)
        return render(request,'testapp/modelformvalidation1.html',{'form':form})

def add_movie_view(request):
    if request.method=="POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('Movie successfully added')
        else:
            return render(request, "testapp/add_movie.html", {'form': form})
    else:

        form = MovieForm(None)
        return render(request, 'testapp/add_movie.html', {'form': form})


