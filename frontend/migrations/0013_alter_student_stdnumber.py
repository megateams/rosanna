# Generated by Django 3.2.17 on 2023-07-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_rename_students_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stdnumber',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Student Number'),
        ),
    ]