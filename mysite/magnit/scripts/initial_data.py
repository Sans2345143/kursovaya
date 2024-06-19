from django.contrib.auth import get_user_model
from magnit.models import Product, LoyaltyLevel, LoyaltyPoints, PurchaseHistory

User = get_user_model()

def run():
    # Create products
    products = [
        {"name": "Product 1", "description": "Description 1", "price": 100, "is_promotion": True},
        {"name": "Product 2", "description": "Description 2", "price": 200, "is_promotion": True},
        {"name": "Product 3", "description": "Description 3", "price": 300, "is_promotion": False},
        {"name": "Product 4", "description": "Description 4", "price": 400, "is_promotion": False},
        {"name": "Product 5", "description": "Description 5", "price": 500, "is_promotion": True},
        {"name": "Product 6", "description": "Description 6", "price": 600, "is_promotion": True},
    ]

    for product in products:
        Product.objects.create(**product)

    # Create loyalty levels
    levels = [
        {"name": "Bronze", "required_points": 100},
        {"name": "Silver", "required_points": 500},
        {"name": "Gold", "required_points": 1000},
    ]

    for level in levels:
        LoyaltyLevel.objects.create(**level)

    # Create a user and loyalty points
    user = User.objects.create_user(username='testuser', password='testpassword')
    LoyaltyPoints.objects.create(user=user, points=150)

    # Create purchase history
    product = Product.objects.first()
    PurchaseHistory.objects.create(user=user, product=product)