from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', label='', label_suffix='', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'E-Mail'}
        ))
    username = forms.CharField(max_length=200, label='', label_suffix='', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        ))
    password1 = forms.CharField(max_length=200, label='', label_suffix='',widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ))
    password2 = forms.CharField(max_length=200, label='', label_suffix='', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Retype Password'}
        ))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(SignupForm, self).save(commit=False)
            user.email = cleaned_data['email']

            if commit:
                user.save()

                return user
