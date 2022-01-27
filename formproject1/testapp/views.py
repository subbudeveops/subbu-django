from django.shortcuts import render
from testapp.forms import BasicForm, HiddenForm

# Create your views here.
def Form_view(request):
  form=BasicForm
  if request.method=="POST":
    form=BasicForm(request.POST)
    if form.is_valid():
      print('name:',form.cleaned_data['name'])
      #print('date:',form.cleaned_data['date']) date is not showing in browser
      print('email:',form.cleaned_data['email'])
      print('feedback:',form.cleaned_data['feedback'])
  return render(request,'testapp/home.html',{'form':form})


#initial how to work on  same form  and render to from manuully
def Manual1_Form_view(request):
  initial_dick={
    'name':'Enter Your Name',
    'email':'Entet The Emailid',
    'feedback':'Enter here Something'
  }
  form=BasicForm(request.POST,initial=initial_dick)
  return render(request,'testapp/manual1.html',{'form':form})
    
def Manual2_Form_view(request):
  form=BasicForm
  if request.method=="POST":
    form=BasicForm(request.POST)
    if form.is_valid():
      print('name:',form.cleaned_data['name'])
      #print('date:',form.cleaned_data['date']) date is not showing in browser
      print('email:',form.cleaned_data['email'])
      print('feedback:',form.cleaned_data['feedback'])
  return render(request,'testapp/manual2.html',{'form':form})



def Manual3_Form_view(request):
  form=BasicForm
  if request.method=="POST":
    form=BasicForm(request.POST)
    if form.is_valid():
      print('name:',form.cleaned_data['name'])
      #print('date:',form.cleaned_data['date']) date is not showing in browser
      print('email:',form.cleaned_data['email'])
      print('feedback:',form.cleaned_data['feedback'])
  return render(request,'testapp/manual3.html',{'form':form})



def Manual4_Form_view(request):
  form=BasicForm
  if request.method=="POST":
    form=BasicForm(request.POST)
    if form.is_valid():
      print('name:',form.cleaned_data['name'])
      #print('date:',form.cleaned_data['date']) date is not showing in browser
      print('email:',form.cleaned_data['email'])
      print('feedback:',form.cleaned_data['feedback'])
  return render(request,'testapp/manual4.html',{'form':form})


def Hidden_Form_view(request):
  form=HiddenForm
  if request.method=="POST":
    form=HiddenForm(request.POST)
    if form.is_valid():
      print('name:',form.cleaned_data['name'])
  return render(request,'testapp/manual5.html',{'form':form})

                        #or 
def Hidden_Form_view(request):
  form=HiddenForm(request.POST)
  return render(request,'testapp/manual5.html',{'form':form})
  