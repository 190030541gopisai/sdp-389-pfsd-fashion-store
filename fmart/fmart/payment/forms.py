from django import forms
from .models import Payment,Card,Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address','city','zip','state')

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('card_name','credit_card_number','exp_month','exp_year','cvv')
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'