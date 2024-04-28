from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm,ProfileForm
from .models import *



def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = CreateUserForm()
    return render(request, 'register_page.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'Welcome back, {username}! You are now logged in.')
            return redirect('home')  # Adjust the URL name to your home page
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')

    return render(request, 'login_page.html')




from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Profile

@login_required
def profile_view(request):
    # Retrieve the profile associated with the authenticated user
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If profile does not exist, create a new one
        profile = Profile.objects.create(user=request.user, email=request.user.email)

    # Pass the profile instance to the template context
    return render(request, 'profile_view.html', {'profile': profile})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Perform form validation
        if not name or not email or not message:
            messages.error(request, 'Please fill out all fields.')
        else:
            # Save the contact message to the database
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Redirect to the home page with success parameter
            return redirect('home')

    return render(request, 'contact_form.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect to profile page after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})