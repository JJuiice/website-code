# Generated by Django 3.1.5 on 2021-01-30 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210130_0044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-creation_date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='[deleted]', max_length=60),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='[deleted]'),
        ),
    ]
