from django.shortcuts import render, HttpResponse

# Create your views here.
def Fees(request):
    return render(request, "finance/index.html")