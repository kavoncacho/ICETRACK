from django.db import models

class sizeCounts (models.Model):
    half_Pint_Count = models.IntegerField(default=30)
    one_Quart_Count = models.IntegerField(default=30)
    pint_Count = models.IntegerField(default=30)
    half_Gallon_Count = models.IntegerField(default=30)
    gallon_Count = models.IntegerField(default=30)
    #size_Choice = models.CharField(max_length=100)

    def __int__(self):
        return self.sizeCounts
        #return self.size_Choice

class itemFlavor (models.Model):
    item_Flavor = models.CharField(max_length=100)
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

