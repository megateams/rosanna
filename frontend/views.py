from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

# Create your views here.
def home(request):
    return render(request,'frontend/dashboard.html')

def login(request):
    return render(request, 'frontend/login.html')

def students(request):
    return render(request, 'frontend/students.html')

def register(request):
    # if (request == 'POST'):
    #     childsurname = request.POST.get('childusername')
    #     childlastname = request.POST.get('childlastname')
    #     childgender = request.post.get('childgender')
    #     immunized = request.post.get('immunized')
    #     formerschool = request.post.get('formerschool')
    #     passportphoto = request.post.get('passportphoto')
    #     fathersfirstname = request.post.get('fathersfirstname')
    #     fatherslastname = request.post.get('fastherslastname')
    #     fathersphonecontact = request.post.get('fathersphonecontact')
    #     fathersemail = request.post.get('fathersemail')
    #     fathersoccupation = request.post.get('fathersoccupation')
    #     fathersresidence = request.post.get('fathersresidence')
    #     mothersfirstname = request.post.get('mothersfirstname')
    #     motherslastname = request.post.get('motherslastname')
    #     mothersphonecontact = request.post.get('mothersphoncontact')
    #     mothersemail = request.post.get('mothersemail')
    #     mothersoccupation = request.post.get('mothersoccupation')
    #     mothersresidence = request.post.get('mothersresidence')
    #     parentsstay = request.post.get('parentsstay')
    #     fathersstay = request.post.get('fathersphoto')
    #     mothersphoto = request.post.get('mothersphoto')
    #     residencedistrict = request.post.get('residencedistrict')
    #     county = request.post.get('county')
    #     subcounty = request.post.get('subcounty')
    #     parish = request.post.get('parish')
    #     village = request.post.get('village')
    #     otherguardianfirstname = request.post.get('otherguardianfirstname')
    #     otherguardianlastname = request.post.get('otherguardianlastname')
    #     guardianoccupation = request.post.get('guardianoccupation')
    #     guardiancontact = request.post.get('guardiancontact')
    #     guardianresidence = request.post.get('guardianresidence')
    #     guardianphoto = request.post.get('guardianphoto')
    #     comments = request.post.get('comments')
        
    #     registration = Students.objects.create(
    #         childsurname = childsurname ,
    #         childlastname = childlastname ,
    #         childgender = childgender ,
    #         immunized = immunized ,
    #         formerschool = formerschool ,
    #         passportphoto = passportphoto ,
    #         fathersfirstname = fathersfirstname ,
    #         fatherslastname = fatherslastname ,
    #         fathersphonecontact = fathersphonecontact ,
    #         fathersemail = fathersemail ,
    #         fathersoccupation = fathersoccupation ,
    #         fathersresidence = fathersresidence ,
    #         mothersfirstname = mothersfirstname ,
    #         motherslastname = motherslastname ,
    #         mothersphonecontact = mothersphonecontact ,
    #         mothersemail = mothersemail ,
    #         mothersoccupation = mothersoccupation ,
    #         mothersresidence = mothersresidence ,
    #         parentsstay = parentsstay ,
    #         fathersstay = fathersstay ,
    #         mothersphoto = mothersphoto ,
    #         residencedistrict = residencedistrict ,
    #         county = county ,
    #         subcounty = subcounty ,
    #         parish = parish ,
    #         village = village ,
    #         otherguardianfirstname = otherguardianfirstname , 
    #         otherguardianlastname = otherguardianlastname , 
    #         guardianoccupation = guardianoccupation , 
    #         guardiancontact = guardiancontact ,
    #         guardianresidence = guardianresidence , 
    #         guardianphoto = guardianphoto , 
    #         comments = comments
    #     )
        
    #     registration.save()
        
        return HttpResponse('Registration Successfull')






