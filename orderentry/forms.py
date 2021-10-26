from django import forms
from orderentry.models import customerInfo, orderInfo

class customerForm(forms.ModelForm):

    customer_first_name = forms.CharField(max_length=30)
    customer_last_name = forms.CharField(max_length=30)
    shipping_address = forms.CharField(max_length=60)
    billing_address = forms.CharField(max_length=60)

    class Meta:
        model = customerInfo
        fields = ('customer_first_name','customer_last_name','shipping_address', 'billing_address',)
    