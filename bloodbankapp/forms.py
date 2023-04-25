
from django import forms
from .models import Donor, BloodBag, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'


class BloodBagForm(forms.ModelForm):
    class Meta:
        model = BloodBag
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields =  ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'blood_group')
