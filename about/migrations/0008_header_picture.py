# Generated by Django 3.1.5 on 2021-02-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_remove_pe_additional_time_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='picture',
            field=models.ImageField(default='/static/headshot.jpg', upload_to='header/'),
        ),
    ]
