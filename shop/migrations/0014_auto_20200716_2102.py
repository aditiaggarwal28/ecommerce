# Generated by Django 3.0.7 on 2020-07-16 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200716_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='product_id',
            new_name='pay_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='product_name',
            new_name='person_name',
        ),
    ]