from email import message
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
# Create your views here.

def Contactform(request):
    
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks For Ur FeedBack!!')
        else:
            messages.warning(request,("There was an error, Please try again!"))
    else:
        form=ContactForm()
    return render(request, 'Contactus.html', {
            'form':form,
    })
