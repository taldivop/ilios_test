# Generated by Django 4.2.3 on 2023-07-05 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_rental_options_rename_vehicle_rental_car'),
        ('cars', '0002_rename_car_vehicle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vehicle',
            new_name='Car',
        ),
    ]
