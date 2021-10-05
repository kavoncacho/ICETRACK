from django.db import models
from inventory import itemFlavor, sizeCounts

class customerInfo (models.Model):
    customer_name = models.CharField(max_length=30)
    shipping_address = models.CharField(max_length=60)
    billing_address = models.CharField(max_length=60)
    customer_status = models.CharField(max_length = 20)

class orderInfo (models.Model):
    order_Item_Flavor = models.CharField(max_length = 20)
    order_Item_Size = models.CharField(max_length = 20)
    order_Item_Quantity = models.IntegerField(default=0)
    order_Item_Shipping = models.CharField(max_length = 20)
    order_date = models.DateTimeField('order date')
    total_Cost = models.IntegerField(default=0)
