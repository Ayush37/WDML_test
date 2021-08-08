# Generated by Django 2.2.4 on 2021-08-08 03:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('view_wdml', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product_name',
            field=models.CharField(default=datetime.datetime(2021, 8, 8, 3, 31, 50, 255728, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product_price',
            field=models.FloatField(default=37),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product_quantity',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]