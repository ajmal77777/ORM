from django.shortcuts import render
from .models import food_delivery_db


def index(request):
    orders = food_delivery_db.objects.all().order_by('order_id')
    context = {'orders': orders}
    return render(request, 'myapp/index.html', context)
