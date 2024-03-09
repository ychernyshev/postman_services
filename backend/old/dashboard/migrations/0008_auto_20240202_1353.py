# Generated by Django 3.2.23 on 2024-02-02 13:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_letteritemmodel_expired_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='letteritemmodel',
            name='letter_image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='letteritemmodel',
            name='expired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 2, 13, 53, 0, 548700, tzinfo=utc)),
        ),
    ]
