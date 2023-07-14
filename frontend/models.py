from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('m' , 'Male'),
    ('f' , 'Female'),
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

IMMUNIZED_CHOICES = [
    ('yes' , 'yes'),
    ('no' , 'no')
]

PARENTS_CHOICES = [
    ('yes' , 'yes'),
    ('no' , 'no')
]

class Registration(models.Model):
    childsurname = models.CharField(max_length = 25 , verbose_name = 'Child Surname')
    childlastname = models.CharField(max_length = 25 , verbose_name = 'Child Last name' )
    childgender = models.CharField(max_length=1 , choices= GENDER_CHOICES , verbose_name = 'Choose Gender')
    appliedclass = models.CharField(max_length= 6 , choices= CLASS_CHOICES , verbose_name= 'Class Applied for')
    immunized = models.CharField(max_length= 3, choices=IMMUNIZED_CHOICES , verbose_name= 'Was your child immunized?' )
    formerschool = models.CharField(max_length=50 , verbose_name="Former School")
    passportphoto = models.ImageField(verbose_name='Childs Passport photo' , upload_to='imagesfiles')
    fathersfirstname  = models.CharField(max_length=25 , verbose_name="Fathers First Name")
    fatherslastname = models.CharField(max_length= 25 , verbose_name= 'Fathers last name')
    fathersphonecontact = models.CharField(max_length=20 , verbose_name='Phone Contact')
    fathersemail = models.EmailField(max_length= 30 , verbose_name='Fathers email')
    fathersoccupation = models.CharField(max_length= 25 , verbose_name='occupation')
    fathersresidence = models.CharField(max_length= 25 , verbose_name='Residence')
    mothersfirstname  = models.CharField(max_length=25 , verbose_name="Mothers First Name")
    motherslastname = models.CharField(max_length= 25 , verbose_name= 'Mothers last name')
    mothersphonecontact = models.CharField(max_length=20 , verbose_name='Phone Contact')
    mothersemail = models.EmailField(max_length= 30 , verbose_name='Mothers email')
    mothersoccupation = models.CharField(max_length= 25 , verbose_name='occupation')
    mothersresidence = models.CharField(max_length= 25 , verbose_name='Residence')
    parentsstay = models.CharField(max_length= 3 , choices= PARENTS_CHOICES , verbose_name='Do both parents stay together?' )
    fathersphoto = models.ImageField(verbose_name= 'Fathers passport photo' , upload_to='imagesfile')
    mothersphoto = models.ImageField(verbose_name= 'Mothers passport photo' , upload_to='imagesfile')
    residencedistrict = models.CharField(max_length= 25 , verbose_name= 'district of Residence')
    county = models.CharField(max_length=25 , verbose_name='County')
    subcounty = models.CharField(max_length=25 , verbose_name='subcounty')
    parish = models.CharField(max_length=25 , verbose_name='parish')
    village = models.CharField(max_length=25 , verbose_name='village/ zone')
    otherguardianfirstname = models.CharField(max_length=25 , verbose_name='Other Guardian First name')
    otherguardianlastname = models.CharField(max_length=25 , verbose_name='Other Guardians LAst name')
    guardianoccupation = models.CharField(max_length= 25 , verbose_name='Guardian occupation')
    guardiancontact = models.CharField(max_length=20 , verbose_name="Guardian Contact")
    guardianresidence = models.CharField(max_length= 25 , verbose_name='Guardians Residence')
    guardianphoto = models.ImageField(verbose_name='Guardians Photo' , upload_to='imagesfile')
    comments = models.TextField(verbose_name='Comments')
    
    Display_Fields = [
        'childsurname' , 'childlastname' , 'childgender' , 'appliedclass' , 'immunized' , 'formerschool' , 'passportphoto' ,
        'fathersfirstname' , 'fatherslastname' , 'fathersphonecontact' , 'fathersemail' , 'fathersoccupation' , 'fathersresidence',
        'mothersfirstname' , 'motherslastname' , 'mothersphonecontact' , 'mothersemail' , 'mothersoccupation' ,
        'mothersresidence' , 'parentsstay' , 'fathersphoto' , 'mothersphoto' , 'residencedistrict' , 'county' , 'subcounty',
        'parish' , 'village' , 'otherguardianfirstname' , 'otherguardianlastname' , 'guardianoccupation' , 'guardiancontact' ,
        'guardianresidence' , 'guardianphoto' , 'comments'
    ]






