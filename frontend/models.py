from django.db import models
from datetime import date
# Create your models here.

GENDER_CHOICES = [
    ('m' , 'Male'),
    ('f' , 'Female'),
]

TERM_CHOICES = [
    ('I' , 'I'),
    ('II' , 'II'),
    ('III' , 'III'),
]

CLASS_CHOICES =[
    ('baby' , 'baby'),
    ('middle' , 'middle'),
    ('top' , 'top'),
    ('P.1' , 'P.1'),
    ('P.2' , 'P.2'),
    ('P.3' , 'P.3'),
    ('P.4' , 'P.4'),
    ('P.5' , 'P.5'),
    ('P.6' , 'P.6'),
    ('P.7' , 'P.7')
]

# IMMUNIZED_CHOICES = [
#     ('yes' , 'yes'),
#     ('no' , 'no')
# ]

# PARENTS_CHOICES = [
#     ('yes' , 'yes'),
#     ('no' , 'no')
# ]

class Students(models.Model):
    stdnumber = models.CharField(primary_key=True , max_length=20 , verbose_name='Student Number' , blank= True)
    regdate = models.DateField(verbose_name='Date', default=None, blank=True )
    childname = models.CharField(max_length=25 , verbose_name="Child's Name" , blank=True)
    gender = models.CharField(max_length=10 , verbose_name="Child's Gender" , blank=True)
    dob = models.DateField(verbose_name='Date of Birth' , blank=True , default= None)
    address = models.CharField(max_length=20 , verbose_name='Address' , blank=True)
    house = models.CharField(max_length=20 , verbose_name='House' , blank=True)
    studentclass = models.CharField(choices=CLASS_CHOICES , max_length=6 , verbose_name='Class' , blank=True)

    fathername = models.CharField(max_length=25 , verbose_name="Father's Name" , blank=True)
    fcontact = models.CharField(max_length=10 , verbose_name="Father's Contact" , blank=True)
    foccupation = models.CharField(max_length=20 , verbose_name="Father's Occupation" , blank=True)

    mothername = models.CharField(max_length=25 , verbose_name="Mother's Name" , blank=True)
    mcontact = models.CharField(max_length=10 , verbose_name="Mother's Contact" , blank=True)
    moccupation = models.CharField(max_length=20 , verbose_name="Mother's Occupation" , blank=True)
    livingwith = models.CharField(max_length=20 , verbose_name="Living With" , blank=True)

    guardianname = models.CharField(max_length=10 , verbose_name='Guardian Names' , blank=True)
    gcontact = models.CharField(max_length=10 , verbose_name="Guardian's Contact" , blank=True)

    Display_Fields = [
        'stdnumber','childname' , 'gender' , 'dob' , 'address' , 'house' , 'studentclass' , 'foccupation' , 'mothername'
    , 'mcontact' , 'moccupation' , 'livingwith' , 'guardianname' , 'gcontact' 
    ]

class Subjects(models.Model):
    subjectname = models.CharField(max_length = 25 , verbose_name = 'Subject Name')
    subjectid = models.CharField(primary_key=True , max_length = 25 , verbose_name = 'Subject id')
    classlevel = models.CharField(max_length = 25 , verbose_name = 'Class Level')
    subjecthead = models.CharField(max_length = 25 ,  verbose_name = "Head of Subject")

    Display_Subjects = [
        'subjectname' , 'subjectid' , 'classlevel' , 'subjecthead'
    ]

class Schoolclasses(models.Model):
    subjects = models.ManyToManyField(Subjects)
    classname = models.CharField(max_length =20 , verbose_name = "Class Name")
    classid = models.CharField(primary_key=True , max_length = 10 , verbose_name = "Class id")
    classteacher = models.CharField(max_length = 10 , verbose_name = "Classteacher")
    numofstds = models.CharField(max_length = 4 , verbose_name = 'Number of Students')

    Display_schoolclasses = [
        'classname' , 'classid' , 'classteacher' , 'numofstds'
    ]

class Teachers(models.Model):
    classrelationship = models.ManyToManyField(Schoolclasses)
    subjectrelationship = models.ManyToManyField(Subjects)

    teacherid = models.CharField(primary_key=True , max_length= 10 , verbose_name='Teacher id')
    teachernames = models.CharField(max_length=25 , verbose_name='Teachers Names')
    dob = models.DateField(default=None , verbose_name='Date of Birth')
    gender = models.CharField(max_length=1 , choices=GENDER_CHOICES , verbose_name='Gender')
    contact = models.CharField(max_length=10 , verbose_name='Contact')
    email = models.EmailField(verbose_name="Email Address")
    address = models.CharField(max_length=20 , verbose_name='Address')
    classes = models.CharField(max_length=50 , verbose_name="Classes Taught")
    joiningdate = models.DateField(default=None , verbose_name='Joining Date')
    position = models.CharField(max_length=20 , verbose_name='Position')
    subject = models.CharField(max_length=20 , verbose_name='Subject')
    qualification = models.CharField(max_length=20 , verbose_name='Academic Qualifications')
    username = models.CharField(max_length=20 , verbose_name='Username')
    password = models.CharField(max_length=20 , verbose_name='Password')

    Display_Teachers = [
        'teacherid' , 'teachernames' , 'dob' , 'gender' , 'contact' , 'email' , 'address' , 'classes' , 'joiningdate',
        'position' , 'subject' , 'qualification' , 'username' , 'password' 
    ]

# class primaryonestds(models.Model):
#     stdnumber = models.CharField(primary_key=True , max_length=25 , verbose_name='Student Number')
#     stdname = models.CharField(max_length=25 , verbose_name='Student Name')
    
#     displayprimaryone = [
#         'stdnumber' , 'stdname' 
#     ]
    

class Marks(models.Model):
    stdnum = models.ForeignKey(Students , on_delete=models.CASCADE , default='std_000')
    term = models.CharField(choices= TERM_CHOICES , max_length=3 , verbose_name="Term" , default='I')
    year = models.CharField(max_length=5 , verbose_name='Year' , default='2023')
    studentclass = models.CharField(max_length=10 , choices=CLASS_CHOICES , default='P.7')
    math = models.IntegerField(verbose_name='Math')
    eng = models.IntegerField(verbose_name='Eng')
    sci = models.IntegerField(verbose_name='Sci')
    sst = models.IntegerField(verbose_name='SST')
    re = models.IntegerField(verbose_name='Religious Education' , default=None)
    computer = models.IntegerField(verbose_name='Computer' , default=None)
    
    #stdname = Registration.objects.get(regnum = stdnum)
    #stdmarks - models.IntegerField(verbose_name='Student Marks')
    
    displaymarks = [
        'stdnum', 'year' , 'studentclass' , 'term' ,'math' , 'eng' , 'sci' , 'sst'
    ]


