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
    subjectname = models.CharField(max_length = 25 , verbose_name = 'Subject Name' , blank=True)
    subjectid = models.CharField(primary_key=True , max_length = 25 , verbose_name = 'Subject id' , default='subj_000')
    classlevel = models.CharField(max_length = 25 , verbose_name = 'Class Level' , blank=True)
    subjecthead = models.CharField(max_length = 25 ,  verbose_name = "Head of Subject" , blank=True)

    Display_Subjects = [
        'subjectname' , 'subjectid' , 'classlevel' , 'subjecthead'
    ]

class Schoolclasses(models.Model):
    subjects = models.ManyToManyField(Subjects)
    classname = models.CharField(max_length =20 , blank=True, verbose_name = "Class Name")
    classid = models.CharField(primary_key=True , max_length = 10 , default=None, verbose_name = "Class id")
    classteacher = models.CharField(max_length = 10 , verbose_name = "Classteacher" , blank=True)
    numofstds = models.CharField(max_length = 4 , verbose_name = 'Number of Students' , blank=True)

    Display_schoolclasses = [
        'classname' , 'classid' , 'classteacher' , 'numofstds'
    ]

class Teachers(models.Model):
    classrelationship = models.ManyToManyField(Schoolclasses)
    subjectrelationship = models.ManyToManyField(Subjects)

    teacherid = models.CharField(primary_key=True , max_length= 10 , verbose_name='Teacher id' , default=None)
    teachernames = models.CharField(max_length=25 , verbose_name='Teachers Names' , blank=True)
    dob = models.DateField(default=None , verbose_name='Date of Birth' , blank=True)
    gender = models.CharField(max_length=1 , choices=GENDER_CHOICES , blank=True , verbose_name='Gender')
    contact = models.CharField(max_length=10 , verbose_name='Contact' , blank=True)
    email = models.EmailField(verbose_name="Email Address" , blank=True)
    address = models.CharField(max_length=20 , verbose_name='Address' , blank=True)
    classes = models.CharField(max_length=50 , verbose_name="Classes Taught" , blank=True)
    joiningdate = models.DateField(default=None , verbose_name='Joining Date' , blank=True)
    position = models.CharField(max_length=20 , verbose_name='Position' , blank=True)
    subject = models.CharField(max_length=20 , verbose_name='Subject', blank=True)
    qualification = models.CharField(max_length=20 , verbose_name='Academic Qualifications' , blank=True)
    username = models.CharField(max_length=20 , verbose_name='Username' , blank=True)
    password = models.CharField(max_length=20 , verbose_name='Password' , blank=True)

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


# GENDER_CHOICES = (
#     ('m', 'Male'),
#     ('f', 'Female')
# )

# APPLIED_CLASS_CHOICES = (
#     ('baby', 'Baby'),
#     ('middle', 'Middle'),
#     ('top', 'Top'),
#     ('p1', 'P.1'),
#     ('p2', 'P.2'),
#     ('p3', 'P.3'),
#     ('p4', 'P.4'),
#     ('p5', 'P.5'),
#     ('p6', 'P.6'),
#     ('p7', 'P.7')
# )

# IMMUNIZED_CHOICES = (
#     ('yes', 'Yes'),
#     ('no', 'No')
# )

# PARENTS_CHOICES = (
#     ('yes', 'Yes'),
#     ('no', 'No')
# )

# class Registration(models.Model):
#     childsurname = models.CharField(max_length=25, verbose_name="Child's Surname")
#     childlastname = models.CharField(max_length=25, verbose_name="Child's Lastname")
#     childgender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Choose Gender")
#     appliedclass = models.CharField(max_length=10, choices=APPLIED_CLASS_CHOICES, verbose_name="Class Applied for")
#     immunized = models.CharField(max_length=5, choices=IMMUNIZED_CHOICES, verbose_name='Was your Child immunized?')
#     formerschool = models.CharField(max_length=30, verbose_name="What is your Child's former school?")
#     childphoto = models.ImageField(verbose_name='Choose Passport photo')
#     fathersurname = models.CharField(max_length=25, verbose_name="Father's Surname")
#     fatherlastname = models.CharField(max_length=25, verbose_name="Lastname")
#     fatherphonecontact = models.CharField(max_length=25, verbose_name="Phone Contact")
#     fatheremail = models.EmailField(verbose_name='Email')
#     fatheroccupation = models.CharField(max_length=50, verbose_name="Occupation")
#     fatherresidence = models.CharField(max_length=25, verbose_name="Place of residence")
#     mothersurname = models.CharField(max_length=25, verbose_name="Mother's Surname")
#     motherlastname = models.CharField(max_length=25, verbose_name="Lastname")
#     motherphonecontact = models.CharField(max_length=25, verbose_name="Phone Contact")
#     motheremail = models.EmailField(verbose_name='Email')
#     motheroccupation = models.CharField(max_length=50, verbose_name="Occupation")
#     motherresidence = models.CharField(max_length=25, verbose_name="Place of residence")
#     parents = models.CharField(max_length=5, choices=PARENTS_CHOICES, verbose_name='Do both parents stay together?')
#     fatherphoto = models.ImageField(verbose_name='Passport Photo of the father')
#     motherphoto = models.ImageField(verbose_name='Passport Photo of the mother')
#     childdistrict = models.CharField(max_length=20, verbose_name="District of Residence")
#     childsubcounty = models.CharField(max_length=20, verbose_name='Subcounty/Division')
#     childparish = models.CharField(max_length=20, verbose_name='Parish')
#     childvillage = models.CharField(max_length=20, verbose_name='Village/Zone')
#     guardianfirstname = models.CharField(max_length=30, verbose_name='Other Guardian First name')
#     guardianlastname = models.CharField(max_length=30, verbose_name='Last name')
#     guardianoccupation = models.CharField(max_length=10, verbose_name='Occupation')
#     guardiancontact = models.CharField(max_length=20, verbose_name='Phone Contact')
#     guardianresidence = models.CharField(max_length=50, verbose_name='Place of Residence')

#login model

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female')
)

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

