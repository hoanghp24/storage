# Generated by Django 4.2.3 on 2023-10-10 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_brand_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='supplier_data',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='customer_data',
        ),
    ]