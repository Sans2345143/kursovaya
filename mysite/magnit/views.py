from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def page1(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/main')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = CustomUserCreationForm()
    return render(request, 'magnit/registration1.html', {'form': form})

def page2(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/main')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = CustomAuthenticationForm()
    return render(request, 'magnit/vhodaition.html', {'form': form})

def main(request):
    return render(request, 'main.html')
