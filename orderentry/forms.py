from django import forms
from orderentry.models import customerInfo, orderInfo

class customer_Information(forms.ModelForm):

    customerFirstName = forms.CharField(max_length=30)
    customerLastName = forms.CharField(max_length=30)
    ShippingAddress = forms.CharField(max_length=60)
    BillingAddress = forms.CharField(max_length=60)

    class Meta:
        model = customerInfo
        fields = ('customerFirstName','customerLastName','ShippingAddress', 'BillingAddress',)
    