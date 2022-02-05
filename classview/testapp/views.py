from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import SubbuModel, ListModel
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.


class subbucreate(CreateView):
    model = SubbuModel
    fields = ['title', 'desc']


class SubbuList(ListView):
    model = ListModel
    fields = '__all__'


class SubbuDetail(DetailView):
    model = ListModel
    fields = '__all__'


class SubbuUpdate(UpdateView):
    model = SubbuModel
    fields = '__all__'
    success_url = "/thanks/"


class SubbuDelete(DeleteView):
    model = SubbuModel
    fields = '__all__'
    sucess_url = "/thanks/"
