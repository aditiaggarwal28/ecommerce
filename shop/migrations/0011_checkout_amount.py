# Generated by Django 3.0.7 on 2020-07-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200716_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
