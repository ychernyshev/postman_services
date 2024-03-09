# Generated by Django 3.2.23 on 2024-02-01 08:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20240201_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letteritemmodel',
            name='date_of_receipt',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='letteritemmodel',
            name='expired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 1, 8, 0, 9, 680974, tzinfo=utc)),
        ),
    ]