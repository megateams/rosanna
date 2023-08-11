
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages


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
    if request.method == 'POST':
        classname = request.POST.get('classname')
        amount = request.POST.get('amount')
        Feesstructure.objects.create(classname=classname, amount=amount)
        # messages.success(request, 'Fees Structure added successfully!')

        # Check if the class already exists in the database
        if Feesstructure.objects.filter(classname=classname).exists():
            messages.error(request, f"Class '{classname}' already exists in the Fees Structure.")
        else:
            # If class does not exist, create and save the new Fees Structure entry
            fees_structure = Feesstructure(classname=classname, amount=amount)
            fees_structure.save()
            messages.success(request, f"Fees Structure for class '{classname}' added successfully.")

        return redirect('Add Fees Structure')
    
    return render(request, 'finance/feesstructure/financeaddFeesstructure.html')

def financefeesstructureList(request):
    fees_list = Feesstructure.objects.all()
    context = {
        'fees_list': fees_list,
    }

    return render(request, 'finance/feesstructure/financefeesstructureList.html', context)

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







