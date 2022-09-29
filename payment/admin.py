from django.contrib import admin
from .models import Address,Card,Payment
# Register your models here.

admin.site.register(Address)
admin.site.register(Card)
admin.site.register(Payment)
