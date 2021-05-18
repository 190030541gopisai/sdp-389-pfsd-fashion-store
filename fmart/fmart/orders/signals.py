from django.db.models.signals import  post_save
from django.dispatch import receiver

from payment.models import Payment
from .models import Orders

"""
    signals are used to create profile when user is creaded
    signals make profile creation automatically  
"""

@receiver(post_save,sender=Payment)
def create_orders(sender,instance,created,**kwargs):
    if created:
        """
            payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    order_status = models.CharField(default="ordered",max_length=10,choices=status)
    order_date =  models.DateField(default=datetime.now)
    shipping_date =
        """
        order_status="ordered"
        order_date = datetime.now()
        shipping_date = datetime.now()+timedelta(days=10)
        Orders.objects.create(payment=instance,
                              order_status=order_status,
                              order_date = order_date,
                              shipping_date = shipping_date
                            )
        print("profile created")

