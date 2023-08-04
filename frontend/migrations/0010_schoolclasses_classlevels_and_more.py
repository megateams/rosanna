# Generated by Django 4.2.3 on 2023-08-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_alter_student_studentclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolclasses',
            name='classlevels',
            field=models.CharField(blank=True, max_length=20, verbose_name='Classlevel'),
        ),
        migrations.AlterField(
            model_name='schoolclasses',
            name='classlevel',
            field=models.CharField(blank=True, max_length=20, verbose_name='Class Level'),
        ),
    ]