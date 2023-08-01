# Generated by Django 4.2.2 on 2023-08-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20230731_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='contact',
            field=models.CharField(max_length=255, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='position',
            field=models.CharField(max_length=255, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='qualification',
            field=models.CharField(blank=True, max_length=255, verbose_name='Academic Qualifications'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='teachernames',
            field=models.CharField(max_length=255, verbose_name='Teachers Names'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='username',
            field=models.CharField(blank=True, max_length=255, verbose_name='Username'),
        ),
    ]
