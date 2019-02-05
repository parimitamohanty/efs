from django import forms
from .models import Customer, Stock, Investment, Mutualfund
from django import forms


class LoginForm(forms.Form):
     username = forms.CharField()
     password = forms.CharField(widget=forms.PasswordInput)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)

class StockForm(forms.ModelForm):
   class Meta:
       model = Stock
       fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)

class InvestmentForm(forms.ModelForm):
   class Meta:
       model = Investment
       fields = ('customer', 'category','description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')

class MutualfundForm(forms.ModelForm):
    class Meta:
        model = Mutualfund
        fields = (
            'customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
            'recent_date',)