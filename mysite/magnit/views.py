import logging
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import CustomUser, generate_unique_id, Product, Statistics
import qrcode
import io
import base64
from django.http import HttpResponse


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
    products = Product.objects.all()
    stats = Statistics.objects.first()  # Assuming you have only one instance

    context = {
        'user': request.user,  # Assuming you want to pass the logged-in user to the template
        'products': products,
        'stats': stats,
        'message': 'Добро пожаловать на главную страницу!',
    }
    return render(request, 'main.html', context)


def logout_view(request):
    logout(request)
    from django.urls import reverse
    return HttpResponseRedirect(reverse('login'))


def profile_view(request):
    user = request.user
    unique_id = user.unique_id

    context = {
        'user': user,
        'unique_id': unique_id,
    }
    return render(request, 'profile.html', context)


def generate_qr_code(request, unique_id):
    try:
        qr = qrcode.QRCode(
            version=1,  # Adjust version as needed
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Choose error correction level
            box_size=10,  # Adjust box size for image resolution
            border=4,  # Adjust border width
        )
        qr.add_data(unique_id)  # Add unique_id data
        qr.make(fit=True)  # Generate QR code matrix
        img = qr.make_image(fill_color='black', back_color='white')  # Create the image

        # Convert the image to a BytesIO object
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)  # Ensure buffer is at the beginning

        return HttpResponse(img_buffer, content_type='image/png')
    except Exception as e:
        # Handle errors appropriately
        return HttpResponse("Internal Server Error", status=500)

        return HttpResponse(img_buffer, content_type='image/png')
    except Exception as e:
        logging.error(f"Error generating QR code: {e}")
        return HttpResponse("Internal Server Error", status=500)


def get_products(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'products': products})


def get_stats(request):
    stats = Statistics.objects.get(id=1)  # Assuming you have only one instance of Stats
    return render(request, 'main/stats.html', {'statistics': stats})

