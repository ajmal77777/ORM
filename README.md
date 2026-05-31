# Food Delivery Django ORM Project

## Project Structure
```
fooddelivery/
├── manage.py
├── populate_db.py
├── fooddelivery/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/
    ├── __init__.py
    ├── apps.py
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    └── templates/
        └── myapp/
            └── index.html
```

## Setup & Run Instructions

### Step 1: Install Django
```bash
python -m pip install django
```

### Step 2: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Populate Database
```bash
python populate_db.py
```

### Step 4: Run the Server
```bash
python manage.py runserver
```

### Step 5: Open in Browser
- **Home page (orders list):** http://127.0.0.1:8000/
- **Admin panel:**             http://127.0.0.1:8000/admin/

## Model Fields (food_delivery_db)
| Field           | Type         | Description           |
|-----------------|--------------|-----------------------|
| order_id        | AutoField    | Primary Key           |
| customername    | CharField    | Customer's name       |
| orderdate       | DateField    | Date of order         |
| itemname        | CharField    | Food item ordered     |
| orderqty        | IntegerField | Quantity ordered      |
| unitprice       | FloatField   | Price per item        |
| totalamount     | FloatField   | Total order amount    |
| deliveryaddress | CharField    | Delivery location     |

## Sample Data (10 Records — May 6, 2026)
| #  | Customer  | Item           | Price  | Address      |
|----|-----------|----------------|--------|--------------|
| 1  | gokul     | pasta          | ₹50    | chennai      |
| 2  | dhanush   | biriyani       | ₹120   | chennai      |
| 3  | vimal     | parotta        | ₹45    | chennai      |
| 4  | hari      | fried rice     | ₹90    | chennai      |
| 5  | mahith    | egg omelete    | ₹30    | chennai      |
| 6  | pareesh   | egg roast dosa | ₹50    | chennai      |
| 7  | chaitanya | idly sambar    | ₹30    | chennai      |
| 8  | sushanth  | kadai rice     | ₹100   | chennai      |
| 9  | varathan  | poori          | ₹50    | chennai      |
| 10 | ranji     | chappathi      | ₹40    | cherrukannur |

