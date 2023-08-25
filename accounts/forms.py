from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use the default User model
        fields = ('username', 'password1', 'password2')  # Include necessary fields

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'phone_number', 'profile_picture', 'address')
