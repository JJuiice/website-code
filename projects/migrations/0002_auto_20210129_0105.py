# Generated by Django 3.1.5 on 2021-01-29 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectList',
            new_name='Project',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id']},
        ),
    ]