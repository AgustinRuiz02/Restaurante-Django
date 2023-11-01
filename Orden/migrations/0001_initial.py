# Generated by Django 4.2 on 2023-10-29 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Plato', '0001_initial'),
        ('Mesa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mesa.mesa')),
                ('plat0', models.ManyToManyField(to='Plato.plato')),
            ],
        ),
    ]
