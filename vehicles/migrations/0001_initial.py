# Generated by Django 5.1.3 on 2024-11-15 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.marka')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=15, unique=True)),
                ('fuel_type', models.CharField(max_length=20)),
                ('transmission_type', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('mileage', models.IntegerField()),
                ('insurance_expiry', models.DateField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.model')),
            ],
        ),
    ]
