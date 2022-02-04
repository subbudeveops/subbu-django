from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import SubbuModel
from .forms import SubbuForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# Create your views here.


def creative_view(request):
    if request.method == "POST":
        form = SubbuForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks')
    else:
        form = SubbuForm()
        return render(request, 'testapp/creative_view.html', {'form': form})


def list_view(request):
    data = SubbuModel.objects.all()
    dataset = SubbuModel.objects.all(id=id)
    return render(request, 'testapp/list_view.html', {'data': data})


def detail_view(request, id):
    data = SubbuModel.objects.get(id=id)
    return render(request, 'testapp/detail_view.html', {'data': data})


def update_view(request, id):
    obj = SubbuModel.objects.get(id=id)

    form = SubbuForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/'+id)

    return render(request, 'testapp/update_view.html', {'form': form,'obj':obj})

def delete_view(request,id):
    obj=SubbuModel.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return HttpResponse("sucessfully deleted")
    return render(request, 'testapp/delete_view.html', {'obj':obj})