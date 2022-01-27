from django.shortcuts import render
from .forms import FormsetForm
from django.forms import formset_factory
# Create your views here.
def formset_view(request):
    SubbuFormset=formset_factory(FormsetForm,extra=3)
    formset=SubbuFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    return render(request,'testapp/formset.html',{'formset':formset})