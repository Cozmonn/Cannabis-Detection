
from django import forms
from .models import Contact

class contactForm(Contact):
    email = forms.EmailField()
    Fullname = forms.CharField(max_length=255)
    message = forms.CharField(max_length=500)
    class Meta:
        model = Contact 
        fields = '__all__'
    

