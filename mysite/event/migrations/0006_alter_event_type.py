# Generated by Django 4.2 on 2023-04-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_event_options_alter_event_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=255, verbose_name='Тип'),
        ),
    ]
