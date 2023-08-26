from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import UserProfileForm
from .forms import CustomUserCreationForm


# Views
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile')  # Redirect to the appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:profile')  # Redirect to user profile
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect(reverse('accounts:user_login'))


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')  # Redirect to the profile page after editing
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def about(request):
    return render(request, 'accounts/about.html')


