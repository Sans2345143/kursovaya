from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import CustomUser, generate_unique_id


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save user without unique_id
            user.unique_id = generate_unique_id()
            user.save()  # Save user with unique_id
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration1.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Create a form instance from POST data

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authentication logic (e.g., using Django's built-in authentication)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to the main page
                return redirect('main_view')  # Replace with your desired URL
            else:
                # Handle login failure
                messages.error(request, 'Неверный логин или пароль')
                # Return rendered template with form for another login attempt
                context = {'form': form}  # Create and use context
                return render(request, 'vhodaition.html', context)
        else:
            # Handle invalid form data
            messages.error(request, 'Неверный формат данных')

    else:
        # Render login form for GET requests
        form = LoginForm()  # Create an empty form instance for GET requests
        context = {'form': form}  # Create and use context
        return render(request, 'vhodaition.html', context)


def main_view(request):
    #  Your logic for the main page, e.g., get data from models
    context = {'message': 'Добро пожаловать на главную страницу!'}  # Example context data
    return render(request, 'main.html', context)


def logout_view(request):
    logout(request)
    from django.urls import reverse
    return HttpResponseRedirect(reverse('login'))


def profile_view(request):
    user = request.user
    unique_id = user.unique_id

    # Add this line to check the value
    print(f"Unique ID: {unique_id}")

    context = {'user': user}
    return render(request, 'profile.html', context)

from django.http import HttpResponse