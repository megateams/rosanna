# Generated by Django 4.2.2 on 2023-09-12 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_fees_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
