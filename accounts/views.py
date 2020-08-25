from .forms import SignupForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def SignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
