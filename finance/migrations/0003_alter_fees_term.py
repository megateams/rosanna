# Generated by Django 4.2.2 on 2023-09-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_bankdetails_term_bankdetails_year_expenserecord_term_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='term',
            field=models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Term'),
        ),
    ]