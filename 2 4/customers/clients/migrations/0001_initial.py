# Generated by Django 5.0 on 2023-12-21 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('hobby', models.TextField()),
                ('previous_work_place', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefer_brand_name', models.CharField(max_length=20)),
                ('prefer_brand_description', models.TextField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client')),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefer_category_name', models.CharField(max_length=20)),
                ('prefer_category_description', models.TextField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client')),
            ],
        ),
    ]
