# Generated by Django 4.0.4 on 2022-05-21 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0020_remove_service_serdate_alter_service_mobilenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='datetime',
        ),
    ]
