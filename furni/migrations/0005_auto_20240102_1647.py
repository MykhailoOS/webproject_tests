# Generated by Django 3.2.23 on 2024-01-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furni', '0004_auto_20231227_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='description',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
