# Generated by Django 4.2.2 on 2023-08-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_remove_expenserecord_amountrequired_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportstaffpayment',
            name='supportstaffid',
            field=models.CharField(max_length=23, verbose_name='Supportstaff id'),
        ),
    ]