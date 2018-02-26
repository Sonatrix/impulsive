from django.contrib import admin
from .models import Advisor, Category, Subcategory, Order

admin.site.register(Advisor)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Order)

