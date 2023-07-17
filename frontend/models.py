from django.db import models

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
    id =models.AutoField(max_length=10, primary_key=True, verbose_name='Admin ID')
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
    # id =models.AutoField(max_length=10, verbose_name='Admin ID')
    name=models.CharField(max_length=30, blank=True, verbose_name='Full Name')
    contact =models.CharField(max_length=20, blank=True, verbose_name='Phone contact')
    email=models.EmailField(max_length=50, blank=True, verbose_name='Email')
    address=models.CharField(max_length=255, blank=True, verbose_name='Address')
    gender =models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, verbose_name="Gender")
    dob=models.DateField(default=None, verbose_name='Date of Birth')
    qualification=models.CharField(max_length=255, blank=True, verbose_name='Qualification')
    position=models.CharField(max_length=255, blank=True, verbose_name='Position')
    
    Display_Supportstaff =['name','contact','email','address','dob','gender','dob','qualification', 'position']
    



    