# Ex01 Django ORM Web Application

**Date:** 21/05/2025

---

## AIM

To develop a Django Application to store and retrieve data from an E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping (ORM).

---

## DESIGN STEPS

### STEP 1
Clone the project from GitHub.

### STEP 2
Create a new app in the Django project.

### STEP 3
Enter the code for `admin.py` and `models.py`.

### STEP 4
Detect changes and create migration files that describe how to modify the database schema.

### STEP 5
Execute the migration files and update the database schema to match the Django models.

### STEP 6
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7
Apply the migration files of the created app to the database.

### STEP 8
Execute Django admin using localhost and create details for 10 entries.

---

# PROGRAM

## models.py

```python
from django.db import models

class FoodOrder(models.Model):
    Order_ID = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=50)
    RestaurantName = models.CharField(max_length=50)
    FoodItem = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Price = models.FloatField()
    DeliveryAddress = models.CharField(max_length=200)
    OrderStatus = models.CharField(max_length=30)

    def __str__(self):
        return self.CustomerName
```

---

## admin.py

```python
from django.contrib import admin
from .models import FoodOrder

class FoodOrderAdmin(admin.ModelAdmin):
    list_display = (
        'Order_ID',
        'CustomerName',
        'RestaurantName',
        'FoodItem',
        'Quantity',
        'Price',
        'DeliveryAddress',
        'OrderStatus'
    )

admin.site.register(FoodOrder, FoodOrderAdmin)
```

---

# OUTPUT

<img width="1027" height="497" alt="Screenshot 2026-05-21 103043" src="https://github.com/user-attachments/assets/d35567d6-d354-45c9-8af5-213d6d4ef33d" />



---

# RESULT

Thus, the program for creating an E-Commerce website database using Django ORM has been executed successfully.
