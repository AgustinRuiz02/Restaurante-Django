# Generated by Django 4.2 on 2023-10-29 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='plat0',
            new_name='plato',
        ),
    ]
