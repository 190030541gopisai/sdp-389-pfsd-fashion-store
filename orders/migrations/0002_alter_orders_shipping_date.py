# Generated by Django 3.2.2 on 2021-05-18 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='shipping_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 19, 39, 45, 442766)),
        ),
    ]
