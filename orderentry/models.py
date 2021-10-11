from django.db import models
from inventory.models import sizeCounts

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
    
    order_Item_Flavor = models.ForeignKey('inventory.itemFlavor', on_delete=models.CASCADE)
    order_Size_Quantity = models.ForeignKey('inventory.sizeCounts', on_delete=models.CASCADE, default = 0)
    order_Item_Shipping_Choices = [('STANDARD','standard'),('EXPEDITED','expedited'),('2-DAY','2-day')]
    order_Item_Shipping = models.CharField(max_length = 20, choices = order_Item_Shipping_Choices, default="STANDARD")
    order_date = models.DateTimeField('order date')
    total_Cost = models.IntegerField(default=0)

    def __str__(self):
        return '%s, %s, $%s, %s' % (self.order_Item_Flavor, self.order_Size_Quantity, self.total_Cost, self.order_date)