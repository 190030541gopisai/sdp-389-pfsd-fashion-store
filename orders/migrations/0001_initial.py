# Generated by Django 3.2.2 on 2021-05-18 14:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0005_payment_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('ordered', 'ordered'), ('canceled', 'canceled')], default='ordered', max_length=10)),
                ('order_date', models.DateField(default=datetime.datetime.now)),
                ('shipping_date', models.DateTimeField(default=datetime.datetime(2021, 5, 28, 19, 38, 31, 153833))),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
            ],
        ),
    ]
