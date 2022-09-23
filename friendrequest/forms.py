from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'password1', 'password2')
