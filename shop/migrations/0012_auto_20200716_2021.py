# Generated by Django 3.0.7 on 2020-07-16 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_checkout_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
    ]
