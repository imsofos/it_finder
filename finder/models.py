from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    price = models.CharField(max_length=32, verbose_name='قیمت فروش')
    buy_price = models.CharField(max_length=32, verbose_name='قیمت خرید')
    img = models.FileField(upload_to='productImages', blank=True, default='productImages/no_img.png', verbose_name="تصویر")
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='موجودی')
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name
    