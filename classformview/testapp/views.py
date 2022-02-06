from django.shortcuts import render
from .forms import SubbuForm
from django.views.generic.edit import FormView
# Create your views here.
class SubbuFormView(FormView):
    form_class=SubbuForm
    template_name='testapp/subbumodel_form.html'
    success_url="/thanks/"
    