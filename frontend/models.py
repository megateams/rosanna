from django.db import models



GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female')
)

# GENDER_CHOICES = [
#     ('m' , 'Male'),
#     ('f' , 'Female'),
# ]

TERM_CHOICES = [
    ('I' , 'I'),
    ('II' , 'II'),
    ('III' , 'III'),
]

CLASS_CHOICES =(
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
)

#students model
class Student(models.Model):
    stdnumber = models.CharField(primary_key=True , max_length=20 , verbose_name='Student Number' , blank= True)
    regdate = models.DateField(verbose_name='Date', default=None, blank=True )
    childname = models.CharField(max_length=25 , verbose_name="Child's Name" , blank=True)
    gender = models.CharField(max_length=10 , verbose_name="Child's Gender" , blank=True)
    dob = models.DateField(verbose_name='Date of Birth' , blank=True , default= None)
    address = models.CharField(max_length=20 , verbose_name='Address' , blank=True)
    house = models.CharField(max_length=20 , verbose_name='House' , blank=True)
    studentclass = models.CharField(max_length=10, blank=True, choices=CLASS_CHOICES, default=None)
    regdate =models.DateField(verbose_name="Date of Registration")
    
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
        'stdnumber','childname' , 'gender' , 'dob' , 'address' , 'house', 'foccupation' , 'mothername'
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
    classlevels = models.CharField(max_length =20 , verbose_name="Class Levels" , blank=True)
    classid = models.CharField(primary_key=True , max_length = 10 , verbose_name = "Class id")
    classteacher = models.CharField(max_length = 100 , verbose_name = "Classteacher")
    numofstds = models.CharField(max_length = 4 , verbose_name = 'Number of Students')

    Display_schoolclasses = [

        'classname' , 'classid' ,'classteacher', 'numofstds', 'classlevels' 

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
    classes = models.CharField(max_length=50 ,blank=True, verbose_name="Classes Taught")
    joiningdate = models.DateField(default=None , verbose_name='Joining Date')
    position = models.CharField(max_length=20 , verbose_name='Position')
    subject = models.CharField(max_length=20 , blank=True, verbose_name='Subject')
    qualification = models.CharField(max_length=20 , blank=True,  verbose_name='Academic Qualifications')
    username = models.CharField(max_length=20 , blank=True, verbose_name='Username')
    password = models.CharField(max_length=20 , verbose_name='Password')

    Display_Teachers = [
        'teacherid' , 'teachernames' , 'dob' , 'gender' , 'contact' , 'email' , 'address' , 'classes' , 'joiningdate',
        'position' , 'subject' , 'qualification' , 'username' , 'password' 
    ]


class Marks(models.Model):
    #id = models.AutoField(primary_key=True)
    stdnum = models.CharField(max_length=100 , verbose_name='Stud number' ,default='std_000' , blank=True)
    term = models.CharField(choices= TERM_CHOICES , max_length=3 , verbose_name="Term" , default='I' , blank=True)
    year = models.CharField(max_length=5 , verbose_name='Year' , default='2023' , blank=True)
    studentclass = models.CharField(max_length=10 , choices=CLASS_CHOICES , default='P.7' , blank=True)
    math = models.IntegerField(verbose_name='Math' , blank=True)
    eng = models.IntegerField(verbose_name='Eng' , blank=True)
    sci = models.IntegerField(verbose_name='Sci' , blank=True)
    sst = models.IntegerField(verbose_name='SST' , blank=True)
    re = models.IntegerField(verbose_name='Religious Education' , default=None , blank=True)
    computer = models.IntegerField(verbose_name='Computer' , default=None , blank=True)
    
    displaymarks = [
        'stdnum', 'year' , 'studentclass' , 'term' ,'math' , 'eng' , 'sci' , 'sst'
    ]

#login model
class Login(models.Model):
    username =models.CharField(max_length=25, blank=True, verbose_name="Username")
    email =models.EmailField(max_length=254, default=None, verbose_name="Email")
    password =models.CharField(max_length=255, verbose_name='Enter the password')
    
    Display_Login_Fields =['username','email','password']
 #user roles model
class Role_Model(models.Model):
    # id =models.CharField(max_length=10, verbose_name='Role ID')
    rolename =models.CharField(max_length=255, verbose_name='Role Name')
    Display_Roles =['rolename']    

#Admin model   
class Admin_Model(models.Model):
    id =models.AutoField(primary_key=True, verbose_name='Admin ID')
    name=models.CharField(max_length=30, blank=True, verbose_name='Full Name')
    username=models.CharField(max_length=30, blank=True, verbose_name='Username')
    contact =models.CharField(max_length=20, verbose_name='Phone contact')
    email=models.EmailField(max_length=50, blank=True, verbose_name='Email')
    gender =models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, verbose_name="Gender")
    address=models.CharField(max_length=255, blank=True, verbose_name='Address')
    dob=models.DateField(default=None, verbose_name='Date of Birth')
    role =models.OneToOneField(Role_Model, on_delete=models.CASCADE, verbose_name='Role')
    password =models.CharField(max_length=255)
    
    Display_Admins =['id','name','username','contact','email', 'gender','address','dob', 'role']
    
#support staff model
class Supportstaff(models.Model):
    id =models.AutoField(primary_key=True, verbose_name='Staff Number')
    fullname=models.CharField(max_length=30, blank=True, verbose_name='Full Name')
    contact =models.CharField(max_length=20, blank=True, verbose_name='Phone contact')
    email=models.EmailField(max_length=50, blank=True, verbose_name='Email')
    address=models.CharField(max_length=255, blank=True, verbose_name='Address')
    gender =models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, verbose_name="Gender")
    dob=models.DateField(default=None, verbose_name='Date of Birth')
    qualification=models.CharField(max_length=255, blank=True, verbose_name='Qualification')
    position=models.CharField(max_length=255, blank=True, verbose_name='Position')
    
    Display_Supportstaff =['id','fullname','contact','email','address','dob','gender','dob','qualification', 'position']


    
    
    
    
    
    
    
    
    