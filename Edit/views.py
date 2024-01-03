
from django.shortcuts import render, redirect
from django.contrib import messages
from Edit.forms import EditProfileFormUser, EditProfileForm
# Create your views here.

def prof(request):
    if request.method == 'POST':
        Userform = EditProfileFormUser(request.POST, instance=request.user)
        Personnelform = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if Userform.is_valid() and Personnelform.is_valid():
            Userform.save()
            Personnelform.save()
            messages.success(request, ("Successfully Updated"))
            return redirect('prof')
        else:
            messages.warning(request, ("There was an error Updating, Please try again!"))
    else:
        userform = EditProfileFormUser(instance=request.user)
        personnelform = EditProfileForm(instance=request.user.profile)
        return render(request, 'profile.html', {
            'Userform': userform, 'Personnelform': personnelform,
        })