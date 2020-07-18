# Generated by Django 2.2 on 2020-07-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0007_auto_20200715_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AddField(
            model_name='product',
            name='buy_price',
            field=models.CharField(default='', max_length=32, verbose_name='قیمت خرید'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='productImages/no_img.png', upload_to='productImages', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=32, verbose_name='قیمت فروش'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='موجودی'),
        ),
    ]
