# Generated by Django 4.2.2 on 2023-08-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_alter_feesstructure_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenserecord',
            name='expenseid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
