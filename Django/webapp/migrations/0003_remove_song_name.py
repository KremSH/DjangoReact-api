# Generated by Django 3.0.8 on 2020-08-07 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200802_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='Name',
        ),
    ]
