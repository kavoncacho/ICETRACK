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