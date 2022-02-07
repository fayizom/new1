from django.contrib.auth.forms import UserCreationForm

from django import forms
from app1.models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email','phone')