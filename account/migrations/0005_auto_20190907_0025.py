# Generated by Django 2.1 on 2019-09-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_guest_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest_info',
            name='birth_day',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='guest_info',
            name='gender',
            field=models.BooleanField(null=True),
        ),
    ]