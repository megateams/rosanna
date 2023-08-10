
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

# teacherpayments views
def financeaddTeacherpayments(request):
    return render(request,'finance/staffpayments/financeaddTeacherpayments.html')

def financeteacherpaymentsList(request):
    return render(request,'finance/staffpayments/financeteacherpaymentsList.html')
# teacherpayments views
# supportstaffpayments views
def financeaddsupportstaffpayments(request):
    return render(request,'finance/staffpayments/financeaddsupportstaffpayments.html')

def financesupportstaffpaymentsList(request):
    return render(request,'finance/staffpayments/financesupportstaffpaymentsList.html')
# supportstaffpayments views

# expenses views
def financeaddExpenses(request):
    return render(request,'finance/expenses/financeaddExpenses.html')

def financeexpensesList(request):
    return render(request,'finance/expenses/financeexpensesList.html')
# expenses views

def financeReports(request):
    return render(request, 'finance/financeReports.html')

def financeStatistics(request):
    return render(request, 'finance/financeStatistics.html')







