from django.db import models

class sizeCounts (models.Model):
    class Meta:
        verbose_name = "Size Count"
        verbose_name_plural = "Size Counts"

    half_Pint_Count = models.IntegerField(default=30)
    one_Quart_Count = models.IntegerField(default=30)
    pint_Count = models.IntegerField(default=30)
    half_Gallon_Count = models.IntegerField(default=30)
    gallon_Count = models.IntegerField(default=30)

    def __str__(self):
        return 'Half Pint: %s, Quart: %s, Pint: %s, Half Gallon: %s, Gallon: %s' % (self.half_Pint_Count, self.one_Quart_Count, 
        self.pint_Count, self.half_Gallon_Count, self.gallon_Count)


class item (models.Model):
    class Meta:
        verbose_name = "Item Flavor"
        verbose_name_plural = "Item Flavors"

    item_Flavor_Choices = [('CHOCOLATE','chocolate'),('VANILLA', 'vanilla'),('COOKIESNCREME', 'cookiesncreme'), ('STRAWBERRY', 'strawberry')]
    item_Flavor = models.CharField(max_length=100, choices = item_Flavor_Choices)
    size_Counts = models.ForeignKey(sizeCounts, on_delete=models.CASCADE, default = None)
    
    def __str__(self):
        return self.item_Flavor

class receipts (models.Model):
    receipts = models.CharField(max_length = 150)

#Keeps track of who makes changes to the database
class lastChangeMade (models.Model):
    last_Change_Made = models.CharField(max_length = 100)
