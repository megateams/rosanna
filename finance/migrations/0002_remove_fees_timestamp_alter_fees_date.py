# Generated by Django 4.2.2 on 2023-10-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='fees',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
