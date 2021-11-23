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

class flavor (models.Model):
    class Meta:
        verbose_name = "Flavor"
        verbose_name_plural = "Flavors"

    flavor_Choices = [('CHOCOLATE','chocolate'),('VANILLA', 'vanilla'),('COOKIESNCREME', 'cookiesncreme'), ('STRAWBERRY', 'strawberry')]
    flavor = models.CharField(max_length=100, choices = flavor_Choices)

    def __str__(self):
        return '%s Flavor' % self.flavor
    
class prices(models.Model):
    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"

    half_Pint_price = models.IntegerField(default=30)
    one_Quart_price = models.IntegerField(default=30)
    pint_price = models.IntegerField(default=30)
    half_Gallon_price = models.IntegerField(default=30)
    gallon_price = models.IntegerField(default=30)

    def __str__(self):
        return 'Half Pint Price: %s, Quart Price: %s, Pint Price: %s, Half Gallon Price: %s, Gallon Price: %s' % (self.half_Pint_price, self.one_Quart_price, 
        self.pint_price, self.half_Gallon_price, self.gallon_price)

class item (models.Model):
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    flavor = models.ForeignKey(flavor, on_delete=models.CASCADE, default = None)
    size_Counts = models.ForeignKey(sizeCounts, on_delete=models.CASCADE, default = None)
    prices = models.ForeignKey(prices, on_delete=models.CASCADE, default = None)
    
    def __str__(self):
        return '%s' % (self.flavor)

class receipts (models.Model):
    receipts = models.CharField(max_length = 150)
