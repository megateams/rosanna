# Generated by Django 4.2.7 on 2023-12-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_student_nin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='nin',
        ),
        migrations.AddField(
            model_name='student',
            name='lin',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='Lin'),
        ),
    ]
