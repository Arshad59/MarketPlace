# Generated by Django 4.2.3 on 2023-09-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]