# Generated by Django 4.2.2 on 2023-07-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolclasses',
            name='classlevel',
            field=models.CharField(blank=True, max_length=100, verbose_name='Classlevel'),
        ),
        migrations.AlterField(
            model_name='schoolclasses',
            name='classteacher',
            field=models.CharField(max_length=100, verbose_name='Classteacher'),
        ),
    ]
