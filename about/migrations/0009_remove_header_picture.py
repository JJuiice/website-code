# Generated by Django 3.1.5 on 2021-02-12 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_header_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='picture',
        ),
    ]