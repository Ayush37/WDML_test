# Generated by Django 2.2.4 on 2021-08-09 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USWTDB', '0002_auto_20210809_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uswdml',
            name='t_hh',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='uswdml',
            name='t_model',
            field=models.TextField(null=True),
        ),
    ]
