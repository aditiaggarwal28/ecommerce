# Generated by Django 3.0.7 on 2020-07-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='first_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]
