
from django.shortcuts import render, HttpResponse

# Create your views here.
def financedashboard(request):
    return render(request, "finance/financedashboard.html")

# fees views
def financeaddFees(request):
    return render(request,'finance/fees/financeaddFees.html')

def financefeesList(request):
    return render(request,'finance/fees/financefeesList.html')
# fees views

# feesstructure views
def financeaddFeesstructure(request):
    return render(request,'finance/feesstructure/financeaddFeesstructure.html')

def financefeesstructureList(request):
    return render(request,'finance/feesstructure/financefeesstructureList.html')
# feesstructure views

# staffpayments views
def financeaddStaffpayments(request):
    return render(request,'finance/staffpayments/financeaddStaffpayments.html')

def financestaffpaymentsList(request):
    return render(request,'finance/staffpayments/financestaffpaymentsList.html')
# staffpayments views

# expenses views
def financeaddExpenses(request):
    return render(request,'finance/expenses/financeaddExpenses.html')

def financeexpensesList(request):
    return render(request,'finance/expenses/financeexpensesList.html')
# expenses views







