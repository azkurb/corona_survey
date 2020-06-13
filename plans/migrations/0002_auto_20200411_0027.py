# Generated by Django 2.2.12 on 2020-04-11 00:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reimburse',
            name='address_one',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reimburse',
            name='address_two',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reimburse',
            name='city',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reimburse',
            name='state',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reimburse',
            name='zip_code',
            field=models.IntegerField(default=77373, max_length=6, validators=[django.core.validators.MinLengthValidator(6)]),
            preserve_default=False,
        ),
    ]
