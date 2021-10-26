from django import forms

class customer_Information(forms.Form):

    customerFirstName = forms.CharField(max_length=30)
    customerLastName = forms.CharField(max_length=30)
    ShippingAddress = forms.CharField(max_length=60)
    BillingAddress = forms.CharField(max_length=60)
    