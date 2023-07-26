# Generated by Django 4.2.2 on 2023-07-26 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=25, verbose_name='Username')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=255, verbose_name='Enter the password')),
            ],
        ),
        migrations.CreateModel(
            name='Role_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=255, verbose_name='Role Name')),
            ],
        ),
        migrations.CreateModel(
            name='Schoolclasses',
            fields=[
                ('classname', models.CharField(max_length=20, verbose_name='Class Name')),
                ('classid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Class id')),
                ('classteacher', models.CharField(max_length=10, verbose_name='Classteacher')),
                ('numofstds', models.CharField(max_length=4, verbose_name='Number of Students')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stdnumber', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, verbose_name='Student Number')),
                ('childname', models.CharField(blank=True, max_length=25, verbose_name="Child's Name")),
                ('gender', models.CharField(blank=True, max_length=10, verbose_name="Child's Gender")),
                ('dob', models.DateField(blank=True, default=None, verbose_name='Date of Birth')),
                ('address', models.CharField(blank=True, max_length=20, verbose_name='Address')),
                ('house', models.CharField(blank=True, max_length=20, verbose_name='House')),
                ('regdate', models.DateField(verbose_name='Date of Registration')),
                ('fathername', models.CharField(blank=True, max_length=25, verbose_name="Father's Name")),
                ('fcontact', models.CharField(blank=True, max_length=10, verbose_name="Father's Contact")),
                ('foccupation', models.CharField(blank=True, max_length=20, verbose_name="Father's Occupation")),
                ('mothername', models.CharField(blank=True, max_length=25, verbose_name="Mother's Name")),
                ('mcontact', models.CharField(blank=True, max_length=10, verbose_name="Mother's Contact")),
                ('moccupation', models.CharField(blank=True, max_length=20, verbose_name="Mother's Occupation")),
                ('livingwith', models.CharField(blank=True, max_length=20, verbose_name='Living With')),
                ('guardianname', models.CharField(blank=True, max_length=10, verbose_name='Guardian Names')),
                ('gcontact', models.CharField(blank=True, max_length=10, verbose_name="Guardian's Contact")),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('subjectname', models.CharField(max_length=25, verbose_name='Subject Name')),
                ('subjectid', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='Subject id')),
                ('classlevel', models.CharField(max_length=25, verbose_name='Class Level')),
                ('subjecthead', models.CharField(max_length=25, verbose_name='Head of Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Supportstaff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Staff Number')),
                ('fullname', models.CharField(blank=True, max_length=30, verbose_name='Full Name')),
                ('contact', models.CharField(blank=True, max_length=20, verbose_name='Phone contact')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default=None, max_length=1, verbose_name='Gender')),
                ('dob', models.DateField(default=None, verbose_name='Date of Birth')),
                ('qualification', models.CharField(blank=True, max_length=255, verbose_name='Qualification')),
                ('position', models.CharField(blank=True, max_length=255, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('teacherid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Teacher id')),
                ('teachernames', models.CharField(max_length=25, verbose_name='Teachers Names')),
                ('dob', models.DateField(default=None, verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1, verbose_name='Gender')),
                ('contact', models.CharField(max_length=10, verbose_name='Contact')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('address', models.CharField(max_length=20, verbose_name='Address')),
                ('classes', models.CharField(max_length=50, verbose_name='Classes Taught')),
                ('joiningdate', models.DateField(default=None, verbose_name='Joining Date')),
                ('position', models.CharField(max_length=20, verbose_name='Position')),
                ('subject', models.CharField(max_length=20, verbose_name='Subject')),
                ('qualification', models.CharField(max_length=20, verbose_name='Academic Qualifications')),
                ('username', models.CharField(max_length=20, verbose_name='Username')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('classrelationship', models.ManyToManyField(to='frontend.schoolclasses')),
                ('subjectrelationship', models.ManyToManyField(to='frontend.subjects')),
            ],
        ),
        migrations.AddField(
            model_name='schoolclasses',
            name='subjects',
            field=models.ManyToManyField(to='frontend.subjects'),
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III')], default='I', max_length=3, verbose_name='Term')),
                ('year', models.CharField(default='2023', max_length=5, verbose_name='Year')),
                ('studentclass', models.CharField(choices=[('baby', 'baby'), ('middle', 'middle'), ('top', 'top'), ('P.1', 'P.1'), ('P.2', 'P.2'), ('P.3', 'P.3'), ('P.4', 'P.4'), ('P.5', 'P.5'), ('P.6', 'P.6'), ('P.7', 'P.7')], default='P.7', max_length=10)),
                ('math', models.IntegerField(verbose_name='Math')),
                ('eng', models.IntegerField(verbose_name='Eng')),
                ('sci', models.IntegerField(verbose_name='Sci')),
                ('sst', models.IntegerField(verbose_name='SST')),
                ('re', models.IntegerField(default=None, verbose_name='Religious Education')),
                ('computer', models.IntegerField(default=None, verbose_name='Computer')),
                ('stdnum', models.ForeignKey(default='std_000', on_delete=django.db.models.deletion.CASCADE, to='frontend.student')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Admin ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Full Name')),
                ('username', models.CharField(blank=True, max_length=30, verbose_name='Username')),
                ('contact', models.CharField(max_length=20, verbose_name='Phone contact')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default=None, max_length=1, verbose_name='Gender')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('dob', models.DateField(default=None, verbose_name='Date of Birth')),
                ('password', models.CharField(max_length=255)),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='frontend.role_model', verbose_name='Role')),
            ],
        ),
    ]
