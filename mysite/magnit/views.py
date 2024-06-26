import logging
from django.contrib.auth.decorators import login_required
from .models import Product, LoyaltyPoint, PurchaseHistory, LoyaltyLevel
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, PurchaseForm
from .models import CustomUser, generate_unique_id
import qrcode
import io
import base64
from django.http import HttpResponse


def index(request):
    # This function will be called when http://127.0.0.1:8000/ is requested
    context = {
        # Add any variables you want to pass to the template here
    }
    return render(request, 'index.html', context)

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


def history_view(request):
    user = request.user
    purchase_history = PurchaseHistory.objects.filter(user=user)
    context = {
        'user': user,
        'purchase_history': purchase_history,}

    return render(request, 'history.html', {'purchase_history': purchase_history})


def main_view(request):
    user = request.user

    # Filter promotions based on 'is_promotion' field
    promotions = Product.objects.filter(promotions=True)

    # Filter special offers based on 'special_offer' field
    special_offers = Product.objects.filter(special_offers=True)


    unique_id = user.unique_id if user.is_authenticated else None

    context = {
        'user': user,
        'promotions': promotions,
        'special_offers': special_offers,
        'unique_id': unique_id,
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
        logging.error(f"Error generating QR code: {e}")
        return HttpResponse("Internal Server Error", status=500)


@login_required
def purchase_view(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user  # Assign the current user to the purchase instance
            purchase.save()
            return redirect('purchase_confirmation')
    else:
        form = PurchaseForm()

    return render(request, 'purchase.html', {'form': form})


@login_required
def purchase_confirmation(request):
    return render(request, 'purchase_confirmation.html')


def calculate_loyalty_points(user, purchases):
    total_spent = sum(purchase.product.price for purchase in purchases)
    loyalty_point, created = LoyaltyPoint.objects.get_or_create(user=user)
    current_level = loyalty_point.get_loyalty_level()

    if current_level:
        points_earned = (total_spent * current_level.point_percentage) // 100
    else:
        points_earned = 0  # or some default percentage if no levels exist

    loyalty_point.points += points_earned
    loyalty_point.save()


@login_required
def loyalty_view(request):
    loyalty_point, created = LoyaltyPoint.objects.get_or_create(user=request.user)
    current_level = loyalty_point
    return render(request, 'loyalty.html', {'points': loyalty_point.points})