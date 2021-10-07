from django.db import models
from inventory.models import sizeCounts

class customerInfo (models.Model):
    customer_status_choices = [('PREFFERED','preferred'),('OKAY', 'okay'),('SHAKY', 'shaky')]
    customer_name = models.CharField(max_length=30)
    shipping_address = models.CharField(max_length=60)
    billing_address = models.CharField(max_length=60)
    customer_status = models.CharField(max_length=30, choices = customer_status_choices, default="PREFERRED")

    def customerName(self):
        return self.customer_name
    def shipAddr(self):
        return self.shipping_address
    def billAddr(self):
        return self.billing_address
    def customerStatus(self):
        return self.customer_status
    
class orderInfo (models.Model):
    order_Item_Flavor = models.ForeignKey('inventory.itemFlavor', on_delete=models.CASCADE)
    order_Size_Quantity = models.ForeignKey('inventory.sizeCounts', on_delete=models.CASCADE, default = 0)
    order_Item_Shipping = models.CharField(max_length = 20)
    order_date = models.DateTimeField('order date')
    total_Cost = models.IntegerField(default=0)

    def item_Flavor(self):
        return self.order_Item_Flavor
    def item_Size_Quantity(self):
        return self.order_Size_Quantity
    def item_Ship(self):
        return self.order_Item_Shipping
    def item_Arrival(self):
        return self.order_date
    def item_totalCost(self):
        return self.total_Cost