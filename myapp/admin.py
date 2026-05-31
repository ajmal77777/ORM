from django.contrib import admin
from .models import food_delivery_db


@admin.register(food_delivery_db)
class FoodDeliveryAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customername', 'orderdate', 'itemname',
                    'orderqty', 'unitprice', 'totalamount', 'deliveryaddress')
    list_filter = ('orderdate', 'deliveryaddress')
    search_fields = ('customername', 'itemname', 'deliveryaddress')
