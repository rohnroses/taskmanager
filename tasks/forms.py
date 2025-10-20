from django import forms
from .models import Task
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Введите рабочий email')

    class Meta:
        model = User
        fields = ["username" , "email", "password1", "password2"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status' , 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


    