# Generated by Django 3.0.8 on 2020-07-18 11:12

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessManagement', '0007_auto_20200716_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AddField(
            model_name='inventory',
            name='tax_amount',
            field=models.FloatField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
