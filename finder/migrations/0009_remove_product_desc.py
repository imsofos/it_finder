# Generated by Django 2.2 on 2020-07-16 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0008_auto_20200716_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
    ]
