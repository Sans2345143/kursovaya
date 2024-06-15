from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib import messages
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
        form = LoginForm(request.POST)  # Create a form instance from POST data

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authentication logic (e.g., using Django's built-in authentication)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to success page
                return redirect('/main_view')  # Replace with your desired URL
            else:
                # Handle login failure
                messages.error(request, 'Неверный логин или пароль')
                # Return rendered template with form for another login attempt
                return render(request, 'vhodaition.html', {'form': form})
        else:
            # Handle invalid form data
            messages.error(request, 'Неверный формат данных')

    else:
        # Render login form for GET requests
        form = LoginForm()  # Create an empty form instance for GET requests
        context = {'form': form}  # Pass the form to the template context
        return render(request, 'vhodaition.html', context)
def main_view(request):
  # Ваша логика для главной страницы, например, получение данных из моделей
  context = {'message': 'Добро пожаловать на главную страницу!'}  # Пример данных контекста
  return render(request, 'main.html', context)

def logout_view(request):
    logout(request)
    return redirect('register')
