# Generated by Django 4.2 on 2023-04-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_start',
            field=models.DateField(),
        ),
    ]
