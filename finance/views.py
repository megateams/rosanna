
from django.shortcuts import render, HttpResponse

# Create your views here.
def Fees(request):
    return render(request, "finance/index.html")

# Create your views here.

def staffpayments(request):
    return render(request , 'staffpayments.html')







