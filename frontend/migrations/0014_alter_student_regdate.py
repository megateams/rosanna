# Generated by Django 3.2.17 on 2023-07-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_alter_student_stdnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='regdate',
            field=models.DateField(verbose_name='Date of Registration'),
        ),
    ]
