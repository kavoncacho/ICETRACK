from django.db import models
from inventory.models import item, sizeCounts
import uuid

class customerInfo (models.Model):
    class Meta:
        verbose_name = "Customer Information"
        verbose_name_plural = "Customer Information"

    customer_name = models.CharField(max_length=30)
    shipping_address = models.CharField(max_length=60)
    billing_address = models.CharField(max_length=60)
    customer_status_choices = [('PREFFERED','preferred'),('OKAY', 'okay'),('SHAKY', 'shaky')]
    customer_status = models.CharField(max_length=30, choices = customer_status_choices, default="PREFERRED")

    def __str__(self):
        return self.customer_name

class orderInfo (models.Model):
    class Meta:
        verbose_name = "Order Information"
        verbose_name_plural = "Order Information"
    
    order_Item_Flavor = models.ForeignKey('inventory.item', on_delete=models.CASCADE)
    half_Pint_Count = models.IntegerField(default=0)
    one_Quart_Count = models.IntegerField(default=0)
    pint_Count = models.IntegerField(default=0)
    half_Gallon_Count = models.IntegerField(default=0)
    gallon_Count = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    customer = models.ForeignKey(customerInfo, on_delete=models.CASCADE, default = 0)
    
    def __str__(self):
        return '%s, Half Pint: %s, Quart: %s, Pint: %s, Half Gallon: %s, Gallon: %s, $%s' % (self.order_Item_Flavor, 
        self.half_Pint_Count, self.one_Quart_Count, self.pint_Count, self.half_Gallon_Count, self.gallon_Count, 
        self.cost)


class invoice (models.Model):
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this invoice')
    customer = models.ForeignKey(customerInfo, on_delete=models.CASCADE)
    order = models.ForeignKey(orderInfo, on_delete=models.CASCADE)
    order_Item_Shipping_Choices = [('STANDARD','standard'),('EXPEDITED','expedited'),('2-DAY','2-day')]
    order_Item_Shipping = models.CharField(max_length = 20, choices = order_Item_Shipping_Choices, default="STANDARD")
    order_date = models.DateTimeField('order date')
    total_Cost = models.IntegerField(default=0)

    def __str__(self):
        return '%s\'s Invoice' % (self.customer.customer_name)
    