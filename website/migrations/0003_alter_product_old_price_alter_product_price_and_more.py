# Generated by Django 5.0.5 on 2024-05-08 15:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_product_old_price_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default='20000.00', max_digits=999999999999, validators=[django.core.validators.MinValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='10000.00', max_digits=999999999999, validators=[django.core.validators.MinValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, null=True),
        ),
    ]