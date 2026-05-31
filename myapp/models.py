from django.db import models


class food_delivery_db(models.Model):
    order_id = models.AutoField(primary_key=True)
    customername = models.CharField(max_length=100)
    orderdate = models.DateField()
    itemname = models.CharField(max_length=100)
    orderqty = models.IntegerField()
    unitprice = models.FloatField()
    totalamount = models.FloatField()
    deliveryaddress = models.CharField(max_length=200)

    def __str__(self):
        return f"Order {self.order_id} - {self.customername}"

    class Meta:
        db_table = 'food_delivery_db'
