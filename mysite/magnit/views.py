from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration1.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            if not form.is_valid():
                messages.error(request, 'Неверный логин или пароль')  # Используйте messages.error
    else:
        form = LoginForm()

    return render(request, 'vhodaition.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main')
