from django import forms
from .models import Customer,Investment,Stock


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)



class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')

class StockForm(forms.ModelForm):
   class Meta:
       model = Stock
       fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)


choices=INTEGER_CHOICES = [('', '')]

class CurrencyForm(forms.Form):
    source_currency_value = forms.DecimalField(label='Amount')
    source_currency_code = forms.CharField(label='From', widget = forms.Select(choices=INTEGER_CHOICES))
    target_currency_code = forms.CharField(label='To', widget = forms.Select(choices=INTEGER_CHOICES))


    def __init__(self, tuple_country_code, *args, **kwargs):
        # required to set the initial form drop down with choices
        self.tuple_country_code = tuple_country_code
        super(CurrencyForm,self).__init__(*args, **kwargs)

        self.fields['source_currency_code'].widget.choices = self.tuple_country_code
        self.fields['target_currency_code'].widget.choices = self.tuple_country_code

