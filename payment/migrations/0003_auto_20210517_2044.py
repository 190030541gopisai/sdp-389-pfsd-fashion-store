# Generated by Django 3.2.2 on 2021-05-17 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210517_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='address',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='card',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
