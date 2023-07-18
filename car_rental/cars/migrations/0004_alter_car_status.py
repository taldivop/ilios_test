# Generated by Django 4.2.3 on 2023-07-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_vehicle_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Disponível'), (2, 'Manutenção')], default=1, verbose_name='Situação'),
        ),
    ]