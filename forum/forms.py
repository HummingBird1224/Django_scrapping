from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

# also importing user defined django form model
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password1']


class questionCreateForm(ModelForm):
    class Meta:
        model = Question
        # fields = ['category_id', 'question_text']
        fields = "__all__"
