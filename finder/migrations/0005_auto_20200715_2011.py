# Generated by Django 2.2 on 2020-07-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=32),
        ),
    ]
