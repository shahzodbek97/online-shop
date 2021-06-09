# Generated by Django 2.0.5 on 2021-06-07 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Buyurtma', 'verbose_name_plural': 'Buyurtmalar'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Buyurtma elementi', 'verbose_name_plural': 'Buyurtma elmentlari'},
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Shahar'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Familya'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, verbose_name="To'langan"),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=20, verbose_name='Pochta Indeksi'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Yangilangan'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order', verbose_name='Buyurtma'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narx'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product', verbose_name='Mahsulot'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Soni'),
        ),
    ]
