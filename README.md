# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Delivery App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f4f4f4; }
        header { background: #1a6e3f; color: white; padding: 15px 30px; }
        header h1 { font-size: 24px; }
        .container { max-width: 1200px; margin: 30px auto; padding: 0 20px; }
        h2 { margin-bottom: 15px; color: #333; }
        table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
        th { background: #1a6e3f; color: white; padding: 12px 15px; text-align: left; font-size: 13px; }
        td { padding: 10px 15px; border-bottom: 1px solid #eee; font-size: 14px; }
        tr:hover { background: #f9f9f9; }
        .badge { display: inline-block; background: #e0f7ea; color: #1a6e3f; padding: 2px 8px; border-radius: 12px; font-size: 12px; }
    </style>
</head>
<body>
    <header>
        <h1>🍽️ Food Delivery Platform</h1>
    </header>
    <div class="container">
        <h2>All Orders ({{ orders.count }} records)</h2>
        <table>
            <thead>
                <tr>
                    <th>ORDER ID</th>
                    <th>CUSTOMER NAME</th>
                    <th>ORDER DATE</th>
                    <th>ITEM NAME</th>
                    <th>ORDER QTY</th>
                    <th>UNIT PRICE</th>
                    <th>TOTAL AMOUNT</th>
                    <th>DELIVERY ADDRESS</th>
                </tr>
            </thead>
            <tbody>
                {% for order in orders %}
                <tr>
                    <td>{{ order.order_id }}</td>
                    <td>{{ order.customername }}</td>
                    <td>{{ order.orderdate }}</td>
                    <td>{{ order.itemname }}</td>
                    <td>{{ order.orderqty }}</td>
                    <td>₹{{ order.unitprice }}</td>
                    <td><span class="badge">₹{{ order.totalamount }}</span></td>
                    <td>{{ order.deliveryaddress }}</td>
                </tr>
                {% empty %}
                <tr><td colspan="8" style="text-align:center;padding:20px;">No orders found.</td></tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>

~~~

## OUTPUT

<img width="1859" height="957" alt="Screenshot 2026-05-31 214153" src="https://github.com/user-attachments/assets/799cbab3-35d0-469e-af0d-49d76c0e5552" />


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
