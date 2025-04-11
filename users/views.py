from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # or your dashboard page
    else:
        form = UserCreationForm()
    return render(request, 'users/login.html', {
        'signup_form': form,
        'login_form': AuthenticationForm()
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {
        'login_form': form,
        'signup_form': UserCreationForm()
    })

def logout_view(request):
    logout(request)
    return redirect('main:index')