# Generated by Django 2.2.4 on 2021-08-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USWTDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uswdml',
            name='case_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='uswdml',
            name='p_cap',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='uswdml',
            name='p_tnum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='uswdml',
            name='p_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='uswdml',
            name='t_cap',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='uswdml',
            name='x_long',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='uswdml',
            name='y_lat',
            field=models.CharField(max_length=255),
        ),
    ]
