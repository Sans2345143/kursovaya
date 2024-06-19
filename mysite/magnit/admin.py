from django.contrib import admin
from .models import Product, LoyaltyLevel, LoyaltyPoints, PurchaseHistory

admin.site.register(Product)
admin.site.register(LoyaltyLevel)
admin.site.register(LoyaltyPoints)
admin.site.register(PurchaseHistory)

