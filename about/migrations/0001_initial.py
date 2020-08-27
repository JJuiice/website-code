# Generated by Django 3.1 on 2020-08-27 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=30)),
                ('start_period', models.CharField(blank=True, max_length=10)),
                ('start_year', models.CharField(default=2020, max_length=4)),
                ('end_period', models.CharField(default='Present', max_length=10)),
                ('end_year', models.CharField(blank=True, max_length=4)),
                ('details', models.TextField()),
            ],
            options={
                'ordering': ['-start_year'],
            },
        ),
        migrations.CreateModel(
            name='PE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=30)),
                ('additional_time_info', models.CharField(blank=True, max_length=30)),
                ('start_period', models.CharField(blank=True, max_length=10)),
                ('start_year', models.CharField(default=2020, max_length=4)),
                ('end_period', models.CharField(default='Present', max_length=10)),
                ('end_year', models.CharField(blank=True, max_length=4)),
                ('details', models.TextField()),
            ],
            options={
                'ordering': ['-start_year'],
            },
        ),
        migrations.CreateModel(
            name='TechSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'ordering': ['-level', 'name'],
            },
        ),
    ]
