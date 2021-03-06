# Generated by Django 3.0.7 on 2020-07-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200711_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=300)),
                ('Address', models.CharField(default='', max_length=300)),
                ('Address_2', models.CharField(default='', max_length=300)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
        ),
    ]
