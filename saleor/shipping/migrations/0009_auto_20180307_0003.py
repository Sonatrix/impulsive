# Generated by Django 2.0.2 on 2018-03-06 18:33

from django.db import migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0008_auto_20180108_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='price',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, max_digits=12),
        ),
    ]
