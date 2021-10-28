from django import forms
from orderentry.models import customerInfo, orderInfo

class customerForm(forms.ModelForm):

    customer_first_name = forms.CharField(max_length=30, label='First Name')
    customer_last_name = forms.CharField(max_length=30, label='Last Name')
    shipping_address = forms.CharField(max_length=60, label='Shipping Address')
    billing_address = forms.CharField(max_length=60, label='Billing Address')

    class Meta:
        model = customerInfo
        fields = ('customer_first_name','customer_last_name','shipping_address', 'billing_address',)
        
class customerInformation(forms.ModelForm):
    #order_Item_Flavor = forms.MultipleChoiceField(choices=['vanilla','chocolate','strawberry','cookiesncream'])
    half_Pint_Count = forms.IntegerField()
    one_Quart_Count = forms.IntegerField()
    pint_Count = forms.IntegerField()
    half_Gallon_Count = forms.IntegerField()
    gallon_Count = forms.IntegerField()
    cost = forms.IntegerField()

    class Meta:
        model = orderInfo
        fields = ('half_Pint_Count', 'one_Quart_Count', 'pint_Count', 'half_Gallon_Count', 'gallon_Count', 'cost',)