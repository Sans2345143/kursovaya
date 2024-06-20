from django.contrib import admin
from .models import Product, LoyaltyLevel, LoyaltyPoint, PurchaseHistory

admin.site.register(Product)
admin.site.register(LoyaltyLevel)
admin.site.register(LoyaltyPoint)
admin.site.register(PurchaseHistory)

