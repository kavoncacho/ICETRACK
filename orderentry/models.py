from django.db import models
from inventory import itemFlavor, sizeCounts

class customerName (models.Model):
    customer_name = models.CharField(max_length=30)

class shippingAddress (models.Model):
    shipping_address = models.CharField(max_length=60)

class billingAddress (models.Model):
    billing_address = models.CharField(max_length=60)

class customerStatus (models.Model):
    customer_status = models.CharField(max_length = 20)

class orderItemFlavor (models.Model):
    order_Item_Flavor = models.ForeignKey(itemFlavor,on_delete=models.CASCADE)

class orderItemSize (models.Model):
    order_Item_Size = models.ForeignKey(sizeCounts,on_delete=models.CASCADE)

class orderItemQuantity (models.Model):
    order_Item_Quantity = models.ForeignKey(sizeCounts,on_delete=models.CASCADE)

class itemShipping (models.Model):
    order_Item_Shipping = models.CharField(max_length = 20)

class orderDate(models.Model):
    order_date = models.DateTimeField('order date')

class totalCost(models.Model):
    total_Cost = models.IntegerField(default=0)
