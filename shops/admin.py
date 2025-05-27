from django.contrib import admin
from .models import Shop, Rent

class RentInline(admin.TabularInline):
    model = Rent
    extra = 12

class ShopAdmin(admin.ModelAdmin):
    inlines = [RentInline]
    list_display = ('name', 'phone', 'shop_address')
    fields = ('name', 'phone', 'owner_address', 'shop_address')

admin.site.register(Shop, ShopAdmin)
