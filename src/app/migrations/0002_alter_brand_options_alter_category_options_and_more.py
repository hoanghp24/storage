# Generated by Django 4.2.3 on 2023-10-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Nhãn hiệu'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Loại sản phẩm'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Khách hàng'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Tồn kho'},
        ),
        migrations.AlterModelOptions(
            name='inventoryreport',
            options={'verbose_name_plural': 'Báo cáo'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Sản phẩm'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name_plural': 'Ảnh sản phẩm'},
        ),
        migrations.AlterModelOptions(
            name='productvariant',
            options={'verbose_name_plural': 'Phiên bản sản phẩm'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Thuộc tính'},
        ),
        migrations.AlterModelOptions(
            name='purchaseorder',
            options={'verbose_name_plural': 'Nhập hàng'},
        ),
        migrations.AlterModelOptions(
            name='saleorder',
            options={'verbose_name_plural': 'Đơn hàng'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name_plural': 'Nhà cung cấp'},
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name_plural': 'Chi nhánh'},
        ),
        migrations.AlterModelOptions(
            name='warranty',
            options={'verbose_name_plural': 'Thời hạn bảo hành'},
        ),
        migrations.AddField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]