# Generated by Django 4.2.6 on 2023-11-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_promotion_class_id_alter_promotion_promotion_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='promotion_mark',
            field=models.IntegerField(verbose_name='Promotion Mark'),
        ),
    ]
