# Generated by Django 5.1.1 on 2024-09-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamerental', '0002_customer_alter_rental_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='customer',
        ),
        migrations.AddField(
            model_name='rental',
            name='renter_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
