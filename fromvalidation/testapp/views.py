
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def home(request):

    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['info@example.com']

            if cc_myself:
                recipients.append(sender)

                send_mail(subject, message, sender, recipients)
                return HttpResponse('<h1>thanks for submit</h1>')
        else:
            return render(request, 'testapp/contactform.html', {'form': form})
    else:
        form=ContactForm()
        return render(request,'testapp/contactform.html',{'form':form})
