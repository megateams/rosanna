# Generated by Django 4.2.7 on 2023-12-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0016_teachers_nin'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportstaff',
            name='nin',
            field=models.CharField(default=None, max_length=50, verbose_name='Nin'),
        ),
    ]