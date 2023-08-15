
from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from .models import Supportstaff , Staffpayments , ExpenseRecord , Fees , Bankdetails , Receipts , Supportstaffpayment , Teacherspayment , Teachers
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.db.models import Sum
from django.contrib import messages
from frontend.models import Schoolclasses, Student

# Create your views here.
#  Display_Fees = ['paymentid', 'stdnumber', 'stdname', 'studentclass', 'amount', 'balance', 'modeofpayment', 'date']
#Display_ExpenseRecords =['expenseid', 'category', 'amountrequired', 'expensedate', 'amountpaid', 'balance']
#displaystaffpayments = ['staffname' , 'datepaid' , 'salary' , 'amountpaid' , 'balance' , 'position' , 'bankaccnum']
#'staffname' , 'bankname' , 'accnum' , 'accname'
#'receiptnum' , 'transactiondate' , 'amountpaid' , 'item' , 'balance' , 'payername'

def deleteteacherpayment(request , id):
    teacherpayment = Teacherspayment.objects.filter(id = id)
    teacherpayment.delete()
    messages.success(request , 'Payment Deleted Successfully')
    return redirect('teacherpaymentslist')
    
def deletesupportstaffpayment(request , paymentid):
    payid = Supportstaffpayment.objects.filter(paymentid = paymentid)
    payid.delete()
    messages.success(request , "Payment deleted successfully")
    supportstaffinfo = Supportstaffpayment.objects.all()
    return redirect('SupportstaffpaymentsList')
    
    
def financeaddStaffpayments(request):
    if request.method == 'POST':
        supportstaffid = request.POST.get('support-staffid')
        supportstaffname = request.POST.get('support-staffname')
        paymentdate = request.POST.get('datepaid')
        salary = request.POST.get('salary')
        amount = request.POST.get('amount')
        balance = request.POST.get('balance')
        paymentmethod = request.POST.get('paymentmethod')
        bankaccnum = request.POST.get('bankaccnum')
        
        Supportstaffpayment.objects.create(
            supportstaffid = supportstaffid ,
            salary = salary ,
            amountpaid = amount ,
            balance = balance ,
            paymentmethod = paymentmethod ,
            bankaccnum = bankaccnum
        )
        Supportstaffpayment.save()
    return render(request , 'finance/staffpayments/financesupportstaffpaymentsList.html')
        
def receipts(request):
    if request.method == 'POST':
        receiptnum = request.POST.get('receiptnum')
        transactiondate = request.POST.get('transactiondate')
        amountpaid = request.POST.get('amountpaid')
        item = request.POST.get('item')
        balance = request.POST.get('balance')
        payername = request.POST.get('payername')
        
        Receipts.objects.create(
            receiptnum = receiptnum ,
            transactiondate = transactiondate ,
            amountpaid = amountpaid ,
            item = item ,
            balance = balance ,
            payername = payername ,
        )
        
        Receipts.save()
    return render(request, 'finace/financedashboard.html')

def bankdetails(request):
    if request.method == 'POST':
        staffname = request.POST.get('staffname')
        bankname = request.POST.get('bankname')
        accnum = request.POST.get('accnum')
        accname = request.POST.get('accname')
        
        Bankdetails.objects.create(
            staffname = staffname ,
            bankname = bankname ,
            accnum = accnum ,
            accname = accname
        )
        
        Bankdetails.save()
    return render(request , 'finance/financedashboard.html')

def staffpayments(request):
    if request.method == 'POST':
        staffname = request.POST.get('staffname')
        datepaid = request.POST.get('datepaid')
        salary = request.POST.get('salary')
        amountpaid = request.POST,get('amountpaid')
        balance = request.POST.get('balance')
        position = request.POST.get('position')
        bankaccnum = request.POST.get('bankaccnum')
        
        Staffpayments.objects.create(
            staffname = staffname ,
            datepaid = datepaid ,
            salary = salary ,
            amountpaid = amountpaid ,
            balance = balance ,
            position = position ,
            bankaccnum = bankaccnum
        )
        
        Staffpayments.save()
    return render(request , 'finace/financedashboard.html')
        
def expenserecords(request):
    if request.method == 'POST':
        expenseid = request.POST.get('expenseid')
        category = request.POST.get('category')
        amountrequired = request.POST.get('amountrequired')
        expensedate = request.POST.get('expensedate')
        amountpaid = request.POST,get('amountpaid')
        balance = request.POST.get('balance')
        
        ExpenseRecord.objects.create(
            expenseid = expenseid ,
            category = category ,
            amountrequired = amountrequired ,
            expensedate = expensedate ,
            amountpaid = amountpaid ,
            balance = balance
        )
        
        ExpenseRecord.save()
    return render(request , 'finance/financedashboard.html')
    
def Fees(request):
    if request.method == 'POST':
        paymentid = request.POST.get('paymentid')
        stdnumber = request.POST.get('stdnumber')
        stdname = request.POST.get('stdname')
        studentclass = request.POST.get('studentclass')
        amount = request.POST.get('amount')
        balance = request.POST.get('balance')
        modeofpayment = request.POST.get('modeofpayment')
        date = request.POST.get('date')
        
        Fees.objects.create(
            paymentid = paymentid ,
            stdnumber = stdnumber ,
            stdname = stdname ,
            studentclass = studentclass ,
            amount = amount ,
            balance = balance ,
            modeofpayment = modeofpayment ,
            date = date
        )
        
        Fees.save()
        
    return render(request, "finance/index.html")


# Create your views here.
def financedashboard(request):
    expenses = ExpenseRecord.objects.all()
    total_amount_paid = expenses.aggregate(Sum('amountpaid'))['amountpaid__sum']
    return render(request, "finance/financedashboard.html", {'total_amount_paid': total_amount_paid})


# fees views
def financeaddFees(request):
    if request.method == 'POST':
        stdnumber = request.POST.get('stdnumber')
        stdname = Student.objects.get(stdnumber=stdnumber).childname  # Get student name
        studentclass = request.POST.get('studentclass')
        classfees = request.POST.get("classfees")
        amount = request.POST.get("amount") # Get amount from fees structure
        balance = int(classfees) - int(amount)
        modeofpayment = request.POST.get('modeofpayment')
        date = request.POST.get('date')
        
        if amount >= classfees:
            # Create a new Fees object and save it to the database
            fees = Fees(
                stdnumber_id=stdnumber,
                stdname=stdname,
                studentclass=studentclass,
                amount=amount,
                balance=balance,
                modeofpayment=modeofpayment,
                date=date
            )
            fees.save()

            messages.success(request, 'Fees registered successfully.')
            return redirect('Add Fees')
        
        else:
            messages.error(request, 'Amount is greater than the class fees. Please try again')
    students = Student.objects.all()
    fees_structures = Feesstructure.objects.all()
    return render(request, 'finance/fees/financeaddFees.html', {'students': students, 'fees_structures': fees_structures})


def financefeesList(request):
    fees_list = Fees.objects.all()
    return render(request,'finance/fees/financefeesList.html',{'fees_list': fees_list})
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
    teacherdetails = Teachers.objects.all()
    if request.method == 'POST':
        teacherid = request.POST.get('teacherid')
        teachername = request.POST.get('teachername')
        paymentdate = request.POST.get('datepaid')
        salary = request.POST.get('salary')
        amountpaid = request.POST.get('amount')
        balance = request.POST.get('balance')
        paymentmethod = request.POST.get('paymentmethod')
        bankaccnum = request.POST.get('bankaccnum')
        
        Teacherspayment.objects.create(
            teacherid = teacherid ,
            teachername = teachername ,
            paymentdate = paymentdate ,
            salary = salary ,
            amountpaid = amountpaid ,
            balance = balance ,
            paymentmethod = paymentmethod ,
            bankaccnum = bankaccnum 
        )
        
        Teacherspayment.save
        messages.success(request , "Teacher Payments added successfully")
        
    return render(request,'finance/staffpayments/financeaddTeacherpayments.html'  , {'teachers':teacherdetails})

def financeteacherpaymentsList(request):
    teachers = Teacherspayment.objects.all()
    return render(request,'finance/staffpayments/financeteacherpaymentsList.html' , {'teachers':teachers})
# teacherpayments views
# supportstaffpayments views
def financeaddsupportstaffpayments(request):
    supportstaffdetails = Supportstaff.objects.all()
    if request.method == 'POST':
        staffid = request.POST.get('support-staffid')
        paymentdate = request.POST.get('datepaid')
        salary = request.POST.get('salary')
        amountpaid = request.POST.get('amount')
        balance = request.POST.get('balance')
        paymentmethod = request.POST.get('paymentmethod')
        bankaccnum = request.POST.get('bankaccnum')
        staffname = request.POST.get('support-staffname')
        
        Supportstaffpayment.objects.create(
            supportstaffid = staffid ,
            staffname = staffname ,
            paymentdate = paymentdate ,
            salary = salary ,
            amountpaid = amountpaid ,
            balance = balance ,
            paymentmethod = paymentmethod ,
            bankaccnum = bankaccnum 
        )
        
        Supportstaffpayment.save
        messages.success(request , "Support Staff payment added Successfully")
    return render(request,'finance/staffpayments/financeaddsupportstaffpayments.html' , {'ids':supportstaffdetails})

def financesupportstaffpaymentsList(request):
    supportstaffinfo = Supportstaffpayment.objects.all()
    return render(request,'finance/staffpayments/financesupportstaffpaymentsList.html' , {'supportstaffdata':supportstaffinfo})
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
    total_amount_paid = ExpenseRecord.objects.aggregate(Sum('amountpaid'))['amountpaid__sum']
    expenses = ExpenseRecord.objects.all()
    context = {
        'expenses': expenses,
        'total_amount_paid': total_amount_paid,
    }
    return render(request, 'finance/expenses/financeexpensesList.html', context)

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


from django.core import serializers
from django.http import JsonResponse

def get_stdclass(request, stdnumber):
    try:
        student = Student.objects.get(stdnumber=stdnumber)
        classname =  student.stdclass.classname

        fees_structure = Feesstructure.objects.get(classname = classname)
        amount = fees_structure.amount
        
        class_data = {
            'classname': classname,
            'amount': amount
        }
        return JsonResponse(class_data)
    except Student.DoesNotExist:
        return JsonResponse({}, status=404)








