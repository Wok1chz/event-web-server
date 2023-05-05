# Generated by Django 4.2 on 2023-04-29 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_event_date_end_alter_event_date_start'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='eventuser',
            name='event_id',
        ),
        migrations.AddField(
            model_name='eventuser',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='event.event'),
        ),
    ]
