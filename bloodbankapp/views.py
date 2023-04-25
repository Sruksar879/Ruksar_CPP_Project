from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Donor, BloodBag, Profile
from django.http import HttpResponseRedirect
from .forms import DonorForm, BloodBagForm, ProfileForm, CreateUserForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'login.html')


#@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


#@login_required
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin') 
    return render(request, 'home.html')

def afterlogin_view(request):
    return redirect('dashboard')

def admin_dashboard_view(request):    
    donors = Donor.objects.all()
    blood_bags = BloodBag.objects.all()
    context = {
        'donors': donors,
        'blood_bags': blood_bags,
    }
    return render(request, 'dashboard.html', context)


#@login_required
def add_donor(request):
    form = DonorForm()
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'add_donor.html', context)


#@login_required
def add_blood_bag(request):
    form = BloodBagForm()
    if request.method == 'POST':
        form = BloodBagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'add_blood_bag.html', context)
        
# def register(request):
#     user_form = UserForm()
#     profile_form = ProfileForm()
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user_form.cleaned_data['password'])
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             messages.success(request, 'User account created successfully')
#         return redirect('login')
#     context = {'user_form': user_form, 'profile_form': profile_form}
#     return render(request, 'register.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:    
        form = CreateUserForm()
        if request.method == 'POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
        context = {'form': form}
        return render(request, 'register.html', context)
    