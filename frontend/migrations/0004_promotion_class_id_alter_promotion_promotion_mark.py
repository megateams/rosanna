# Generated by Django 4.2.5 on 2023-11-16 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='class_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='frontend.schoolclasses'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promotion_mark',
            field=models.CharField(default=None, max_length=10, verbose_name='Promotion Mark'),
        ),
    ]