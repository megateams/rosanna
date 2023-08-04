from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'teacher/dashboard.html')

def profile(request):
    return render(request, 'teacher/profile.html')    

def paymenthistory(request):
    return render(request, 'teacher/paymenthistory.html')   

