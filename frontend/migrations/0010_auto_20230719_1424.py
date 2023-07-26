# Generated by Django 3.2.17 on 2023-07-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_alter_supportstaff_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportstaff',
            old_name='name',
            new_name='fullname',
        ),
        migrations.AlterField(
            model_name='admin_model',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Admin ID'),
        ),
        migrations.AlterField(
            model_name='supportstaff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Staff Number'),
        ),
    ]