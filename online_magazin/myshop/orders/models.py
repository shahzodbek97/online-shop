from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ism')
    last_name = models.CharField(max_length=50, verbose_name='Familya')
    email = models.EmailField(verbose_name='E-mail')
    address = models.CharField(max_length=250, verbose_name='Manzil')
    postal_code = models.CharField(max_length=20, verbose_name='Pochta Indeksi' )
    city = models.CharField(max_length=100, verbose_name='Shahar')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan')
    paid = models.BooleanField(default=False, verbose_name="To'langan")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Buyurtma')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Mahsulot')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Soni')

    class Meta:
        verbose_name = 'Buyurtma elementi'
        verbose_name_plural = 'Buyurtma elmentlari'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
