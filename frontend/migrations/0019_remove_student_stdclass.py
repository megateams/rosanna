# Generated by Django 3.2.17 on 2023-07-25 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_alter_student_stdclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stdclass',
        ),
    ]