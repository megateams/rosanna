
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages
from frontend.models import Schoolclasses


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

        this_class = Feesstructure.objects.filter(classname = classname)
        if(this_class):
            messages.success(request, "This class already exists")
        else:
            fees_structure = Feesstructure.objects.create(classname=classname, amount=amount)
            fees_structure.save()
            messages.success(request, f"Fees Structure for class '{classname}' added successfully.")
        return redirect('Add Fees Structure')
    classes = Schoolclasses.objects.all()
    return render(request, 'finance/feesstructure/financeaddFeesstructure.html',{"classes":classes})

def financefeesstructureList(request):
    fees_list = Feesstructure.objects.all()
    context = {
        'fees_list': fees_list,
    }

    return render(request, 'finance/feesstructure/financefeesstructureList.html', context)

def deletefeesstructure(request, feesstructureid):
    try:
        fees_structure = Feesstructure.objects.get(pk=feesstructureid)
        fees_structure.delete()
        messages.success(request, 'Fees Structure deleted successfully.')
    except Feesstructure.DoesNotExist:
        messages.error(request, 'Fees Structure not found.')
    
    return redirect('Fees Structure List')

def editfeesstructure(request, feesstructureid):
    try:
        fees_structure = Feesstructure.objects.get(pk=feesstructureid)
        if request.method == 'POST':
            updated_classname = request.POST.get('classname')
            updated_amount = request.POST.get('amount')
            
            fees_structure.classname = updated_classname
            fees_structure.amount = updated_amount
            fees_structure.save()
            messages.success(request, 'Fees Structure updated successfully.')
            return redirect('Fees Structure List')
            
        context = {'fees_structure': fees_structure}
        return render(request, 'finance/feesstructure/editfeesstructure.html', context)
    except Feesstructure.DoesNotExist:
        messages.error(request, 'Fees Structure not found.')
        return redirect('Fees Structure List')


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
    
    
    if request.method == 'POST':
        category = request.POST.get('category')
        amountrequired = request.POST.get('amountrequired')
        expensedate = request.POST.get('expensedate')
        amountpaid = request.POST.get('amountpaid')
        balance = request.POST.get('balance')
        
        expense_record = ExpenseRecord(
            category=category,
            amountrequired=amountrequired,
            expensedate=expensedate,
            amountpaid=amountpaid,
            balance=balance
        )
        expense_record.save()
        messages.success(request, 'Expense added successfully.')  # Display a success message
        return redirect('Add Expenses')  # Redirect to expenses list page
    
    return render(request, 'finance/expenses/financeaddExpenses.html')

def financeexpensesList(request):
    expenses = ExpenseRecord.objects.all()
    return render(request, 'finance/expenses/financeexpensesList.html', {'expenses': expenses})

def delete_expense(request, expenseid):
    try:
        expense = ExpenseRecord.objects.get(expenseid=expenseid)
        expense.delete()
        messages.success(request, 'Expense deleted successfully.')
    except ExpenseRecord.DoesNotExist:
        messages.error(request, 'Expense not found.')

    return redirect('Expenses List')

def edit_expense(request, expenseid):
    try:
        expense = ExpenseRecord.objects.get(expenseid=expenseid)
        
        if request.method == 'POST':
            updated_category = request.POST.get('category')
            updated_amountrequired = request.POST.get('amountrequired')
            updated_expensedate = request.POST.get('expensedate')
            updated_amountpaid = request.POST.get('amountpaid')
            updated_balance = request.POST.get('balance')
            
            expense.category = updated_category
            expense.amountrequired = updated_amountrequired
            expense.expensedate = updated_expensedate
            expense.amountpaid = updated_amountpaid
            expense.balance = updated_balance
            expense.save()
            messages.success(request, 'Expense updated successfully.')
            return redirect('Add Expenses')
        
        context = {'expense': expense}
        return render(request, 'finance/expenses/edit_expense.html', context)
    
    except ExpenseRecord.DoesNotExist:
        messages.error(request, 'Expense not found.')
        return redirect('Expenses List')
# expenses views

def financeReports(request):
    return render(request, 'finance/financeReports.html')

def financeStatistics(request):
    return render(request, 'finance/financeStatistics.html')







