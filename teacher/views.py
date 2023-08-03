from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'teacher/dashboard.html')

<<<<<<< HEAD






=======
def profile(request):
    return render(request, 'teacher/profile.html')    

def paymenthistory(request):
    return render(request, 'teacher/paymenthistory.html')   
>>>>>>> ce5469f01d5fcae0a165a8c14673b82339181c8d
