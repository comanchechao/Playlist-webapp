from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def SignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('accouonts/login.html')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hompage.html')

    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', { 'form': form })
