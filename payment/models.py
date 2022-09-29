from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=10)
    zip = models.IntegerField()
    state = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.user.username}'

    # def clean_zip(self):
    #     data = self.cleaned_data['zip']
    #     if len(str(data))!=6:
    #         raise ValidationError("Enter correct Zipcode!")

    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data
    

    # def __str__(self):
    #     return f'{self.user.username} {self.product.p_name} {self.city}'


class Card(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100)
    credit_card_number = models.IntegerField()
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    cvv = models.IntegerField()

    def __str__(self):
        return f'{self.user} {self.credit_card_number}'

    # def clean_credit_card_number(self):
    #     data = self.cleaned_data['credit_card_number']
    #     if len(str(data))!=16:
    #         raise ValidationError("Enter correct credit card number!")
    #     return data


class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.product.p_name}'

    
