# Generated by Django 2.0.5 on 2021-06-06 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Mahsulot', 'verbose_name_plural': 'Mahsulotlar'},
        ),
    ]
