from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('category_name',  'description', )
    list_filter = ('category_name',)
    ordering = ('category_name',)
    
    
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    '''Admin View for Item'''

    list_display  = ('title', 'price', 'discount_price', 'category', 'description',)
    list_filter   = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('name',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


    ordering = ('title',)
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Admin View for OrderItem'''

    list_display = ('id','user', 'ordered', 'item', 'quantity', )
    list_filter  = ('user',)
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ('ref_code','user', 'start_date', 'ordered_date', 'ordered', 'shipping_address', 'billing_address', 'payment', 'coupon', 'being_delivered', 'received', )
    list_filter = ('ref_code','user',)
    
    #search_fields = ('',)
    #date_hierarchy = ''
    #ordering = ('',)
    
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    '''Admin View for Coupon'''

    list_display = ('code', 'amount', )
    
