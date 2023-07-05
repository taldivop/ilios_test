# Generated by Django 4.2.3 on 2023-07-05 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'ordering': ['vehicle', '-pick_up_date', 'drop_off_date'], 'verbose_name': 'Aluguel', 'verbose_name_plural': 'Aluguéis'},
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='car',
            new_name='vehicle',
        ),
    ]
