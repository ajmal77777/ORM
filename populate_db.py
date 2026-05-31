import os
import sys
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fooddelivery.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from myapp.models import food_delivery_db

food_delivery_db.objects.all().delete()

records = [
    {'customername': 'gokul',     'itemname': 'pasta',         'unitprice': 50.0,  'deliveryaddress': 'chennai'},
    {'customername': 'dhanush',   'itemname': 'biriyani',      'unitprice': 120.0, 'deliveryaddress': 'chennai'},
    {'customername': 'vimal',     'itemname': 'parotta',       'unitprice': 45.0,  'deliveryaddress': 'chennai'},
    {'customername': 'hari',      'itemname': 'fried rice',    'unitprice': 90.0,  'deliveryaddress': 'chennai'},
    {'customername': 'mahith',    'itemname': 'egg omelete',   'unitprice': 30.0,  'deliveryaddress': 'chennai'},
    {'customername': 'pareesh',   'itemname': 'egg roast dosa','unitprice': 50.0,  'deliveryaddress': 'chennai'},
    {'customername': 'chaitanya', 'itemname': 'idly sambar',   'unitprice': 30.0,  'deliveryaddress': 'chennai'},
    {'customername': 'sushanth',  'itemname': 'kadai rice',    'unitprice': 100.0, 'deliveryaddress': 'chennai'},
    {'customername': 'varathan',  'itemname': 'poori',         'unitprice': 50.0,  'deliveryaddress': 'chennai'},
    {'customername': 'ranji',     'itemname': 'chappathi',     'unitprice': 40.0,  'deliveryaddress': 'cherrukannur'},
]

for r in records:
    food_delivery_db.objects.create(
        customername=r['customername'],
        orderdate=date(2026, 5, 6),
        itemname=r['itemname'],
        orderqty=1,
        unitprice=r['unitprice'],
        totalamount=r['unitprice'] * 1,
        deliveryaddress=r['deliveryaddress']
    )

print(f"✅ Inserted {food_delivery_db.objects.count()} records successfully!")
for obj in food_delivery_db.objects.all():
    print(f"  [{obj.order_id}] {obj.customername} - {obj.itemname} - ₹{obj.totalamount} - {obj.deliveryaddress}")
