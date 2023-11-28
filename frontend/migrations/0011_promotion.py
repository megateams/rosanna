# Generated by Django 4.2.6 on 2023-11-20 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_delete_promotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_mark', models.IntegerField(verbose_name='Promotion Mark')),
                ('class_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='frontend.schoolclasses')),
            ],
        ),
    ]
