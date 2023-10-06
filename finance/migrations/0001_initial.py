# Generated by Django 4.2.5 on 2023-10-06 06:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.CharField(blank=True, max_length=20, verbose_name='Staff Names')),
                ('bankname', models.CharField(blank=True, max_length=30, verbose_name='Bank Name')),
                ('accnum', models.IntegerField(blank=True, verbose_name='Account Number')),
                ('accname', models.CharField(blank=True, max_length=25, verbose_name='Account Name')),
                ('term', models.CharField(blank=True, default=None, max_length=10, verbose_name='Term')),
                ('year', models.PositiveIntegerField(blank=True, default=None, verbose_name='Year')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseRecord',
            fields=[
                ('expenseid', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=255, verbose_name='Expense category')),
                ('expensedate', models.DateField(verbose_name='Date of Expense')),
                ('amountpaid', models.CharField(blank=True, max_length=20, verbose_name='Amount paid')),
                ('term', models.CharField(blank=True, default=None, max_length=10, verbose_name='Term')),
                ('year', models.PositiveIntegerField(blank=True, default=None, verbose_name='Year')),
            ],
        ),
        migrations.CreateModel(
            name='Feesstructure',
            fields=[
                ('feesstructureid', models.AutoField(primary_key=True, serialize=False)),
                ('classname', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('term', models.CharField(default=None, max_length=10)),
                ('year', models.PositiveIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Supportstaffpayment',
            fields=[
                ('paymentid', models.AutoField(primary_key=True, serialize=False)),
                ('supportstaffid', models.CharField(max_length=10, verbose_name='Support Staff id')),
                ('staffname', models.CharField(max_length=25, null=True, verbose_name='Staffname')),
                ('salary', models.IntegerField(verbose_name='Salary')),
                ('amountpaid', models.IntegerField(verbose_name='Amount Paid')),
                ('paymentdate', models.DateField(max_length=6, null=True, verbose_name='PAyment Date')),
                ('balance', models.IntegerField(verbose_name='Balance')),
                ('accumulatedamount', models.IntegerField(default=None, verbose_name='Accumulated Amount')),
                ('term', models.CharField(blank=True, default=None, max_length=10, verbose_name='Term')),
                ('year', models.PositiveIntegerField(blank=True, default=None, verbose_name='Year')),
            ],
        ),
        migrations.CreateModel(
            name='Teacherspayment',
            fields=[
                ('paymentid', models.AutoField(primary_key=True, serialize=False)),
                ('teacherid', models.CharField(max_length=20, verbose_name='Teacher id')),
                ('teachername', models.CharField(default=None, max_length=30, verbose_name='Teacher Name')),
                ('paymentdate', models.DateField(verbose_name='Payment Date')),
                ('salary', models.IntegerField(verbose_name='Salary')),
                ('amountpaid', models.IntegerField(verbose_name='Amount Paid')),
                ('accumulatedpayment', models.IntegerField(default=None, verbose_name='Accumulated Amount')),
                ('balance', models.IntegerField(verbose_name='Balance')),
                ('term', models.CharField(blank=True, default=None, max_length=10, verbose_name='Term')),
                ('year', models.PositiveIntegerField(blank=True, default=None, verbose_name='Year')),
            ],
        ),
        migrations.CreateModel(
            name='Staffpayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.CharField(blank=True, max_length=25, verbose_name='Staff Name')),
                ('datepaid', models.DateField(blank=True, verbose_name='Payment Date')),
                ('salary', models.IntegerField(blank=True, verbose_name='Salary')),
                ('amountpaid', models.IntegerField(blank=True, verbose_name='Amount Paid')),
                ('balance', models.IntegerField(blank=True, verbose_name='Balance')),
                ('position', models.CharField(blank=True, max_length=15, verbose_name='Position')),
                ('bankaccnum', models.IntegerField(blank=True, default=None, verbose_name='Account Number')),
                ('term', models.CharField(blank=True, default=None, max_length=10, verbose_name='Term')),
                ('year', models.PositiveIntegerField(blank=True, default=None, verbose_name='Year')),
                ('staffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('receiptnum', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, verbose_name='Receipt Number')),
                ('transactiondate', models.DateField(blank=True, verbose_name='Transaction Date')),
                ('amountpaid', models.IntegerField(blank=True, verbose_name='Amount Paid')),
                ('item', models.CharField(blank=True, max_length=30, verbose_name='Item')),
                ('balance', models.IntegerField(blank=True, verbose_name='Balance')),
                ('payername', models.CharField(blank=True, max_length=30, verbose_name='Payer Name')),
                ('term', models.CharField(blank=True, default=None, max_length=10, verbose_name='Term')),
                ('year', models.PositiveIntegerField(blank=True, default=None, verbose_name='Year')),
                ('receipts_staff_relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.teachers')),
                ('recipts_staffpayments_relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.staffpayments')),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('paymentid', models.AutoField(primary_key=True, serialize=False)),
                ('stdname', models.CharField(blank=True, max_length=255, verbose_name='Student name')),
                ('studentclass', models.CharField(blank=True, choices=[('baby', 'baby'), ('middle', 'middle'), ('top', 'top'), ('P.1', 'P.1'), ('P.2', 'P.2'), ('P.3', 'P.3'), ('P.4', 'P.4'), ('P.5', 'P.5'), ('P.6', 'P.6'), ('P.7', 'P.7')], max_length=20, verbose_name='Class')),
                ('classfees', models.CharField(blank=True, max_length=20, verbose_name='Class Fees')),
                ('amount', models.CharField(blank=True, max_length=20, verbose_name='Amount paid')),
                ('accumulatedpayment', models.IntegerField(default=0)),
                ('balance', models.CharField(blank=True, max_length=20, verbose_name='Balance')),
                ('modeofpayment', models.CharField(blank=True, max_length=255, verbose_name='Mode of Payment')),
                ('date', models.DateField(verbose_name='Date of Payment')),
                ('timestamp', models.TimeField(default=django.utils.timezone.now)),
                ('term', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Term')),
                ('year', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Year')),
                ('stdnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.student', verbose_name='Student ID')),
            ],
        ),
    ]
