# Generated by Django 2.1 on 2019-09-07 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190907_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest_info',
            old_name='user_id',
            new_name='user',
        ),
    ]
