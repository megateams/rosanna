
from django.shortcuts import render, HttpResponse
from .models import Staffpayments

# Create your views here.

def Fees(request):
    return render(request, "finance/index.html")

# Create your views here.
def financedashboard(request):
    return render(request, "finance/financedashboard.html")










