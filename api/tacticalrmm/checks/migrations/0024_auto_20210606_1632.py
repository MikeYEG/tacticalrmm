# Generated by Django 3.2.1 on 2021-06-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0023_check_run_interval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkhistory',
            name='check_history',
        ),
        migrations.AddField(
            model_name='checkhistory',
            name='check_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]