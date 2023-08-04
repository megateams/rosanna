# Generated by Django 4.2.3 on 2023-08-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_remove_schoolclasses_classlevels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclasses',
            name='classlevel',
        ),
        migrations.AddField(
            model_name='schoolclasses',
            name='classlevels',
            field=models.CharField(blank=True, max_length=20, verbose_name='Class Levels'),
        ),
    ]