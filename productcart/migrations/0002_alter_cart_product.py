# Generated by Django 4.0.1 on 2022-04-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('productcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]