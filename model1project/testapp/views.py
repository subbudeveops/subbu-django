from django.http import HttpResponse
from django.shortcuts import render
from .forms import SubbuForm
from .models import SubbuModel



# Create your views here.
def home(request):
    if request.method=="POST":
        form=SubbuForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()

            return HttpResponse('sucess')
        else:
            return render(request,'testapp/submit.html',{'form':form})
    else:
        form=SubbuForm(None)
        return render(request,'testapp/submit.html',{'form':form})
        