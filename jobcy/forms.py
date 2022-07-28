from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from accounts.models import University, Student, Application, Program


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ('name','description')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
