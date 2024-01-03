from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class EditProfileFormUser(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username'
        )

class EditProfileForm(ModelForm):
    CNI = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    BadgeID = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    BirthdayDay = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile
        fields = (
            'BadgeID',
            'CNI',
            'BirthdayDay'
        )