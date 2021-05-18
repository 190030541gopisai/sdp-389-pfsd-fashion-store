from django.db import models
from payment.models import Payment
from datetime import datetime  
from datetime import timedelta   


# Create your models here.
class Orders(models.Model):
    status = (
        ('ordered','ordered'),
        ('canceled','canceled')
    )
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    order_status = models.CharField(default="ordered",max_length=10,choices=status)
    order_date =  models.DateField(default=datetime.now)
    shipping_date = models.DateTimeField(default=datetime.now)
    

    #(datetime.now()+timedelta(days=10))
    def __str__(self):
        return f'{self.payment.user.username} {self.id}'