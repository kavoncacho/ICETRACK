from django.db import models

class sizeCounts (models.Model):
    half_Pint_Count = models.IntegerField(default=30)
    one_Quart_Count = models.IntegerField(default=30)
    pint_Count = models.IntegerField(default=30)
    half_Gallon_Count = models.IntegerField(default=30)
    gallon_Count = models.IntegerField(default=30)
    #size_Choice = models.CharField(max_length=100)

    def hpQuant (self):
        return self.half_Pint_Count
    def oqQuant (self):
        return self.one_Quart_Count
    def pQuant (self):
        return self.pint_Count
    def hgQuant (self):
        return self.half_Gallon_Count
    def gQuant (self):
        return self.gallon_Count

class itemFlavor (models.Model):
    item_Flavor_Choices = [('CHOCOLATE','chocolate'),('VANILLA', 'vanilla'),('COOKIESNCREME', 'cookiesncreme'), ('STRAWBERRY', 'strawberry')]
    item_Flavor = models.CharField(max_length=100, choices = item_Flavor_Choices)
    item_Size_Quantity = models.ForeignKey(sizeCounts, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item_Flavor

#Counting how many are dedicated to unfilled orders
class toBeSent (models.Model):
    to_Be_Sent = models.IntegerField(default=0)

class receipts (models.Model):
    receipts = models.CharField(max_length = 150)

#Keeps track of who makes changes to the database
class lastChangeMade (models.Model):
    last_Change_Made = models.CharField(max_length = 100)

