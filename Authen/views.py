# Create your views here.
from distutils.log import error
import email

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse, reverse_lazy
from .form import SignInForm, EditProfileForm


# Create your views here.


#login_view

def logform(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            messages.success(request,("Successfully Logged In"))
            return redirect('dash')
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, ("There was an error Logging In, Please try again!"))
            #return redirect(request, contactus)
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')


#sign_up_view
def register_user(request):
    if request.method=='POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.warning(request,("Please complete ur signing up"))
            return redirect('dash')
        else:
            messages.warning(request,("There was an error Logging In, Please try again!"))
    else:
        form=SignInForm()
    return render(request, 'sig.html', {
            'form':form,
    })


def logoutt(request):
    logout(request)
    messages.success(request, ("Logging Out Successfully"))
    return redirect('login')

@login_required(login_url="login")
def mainDash(request):
    return render(request, 'Dashboard.html')

@login_required(login_url="login")
def edit_profile(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,("Successfully Updated"))
            return redirect('dash')
        else:
            messages.warning(request,("There was an error Updating, Please try again!"))         
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit.html', {
        'form':form,
    })