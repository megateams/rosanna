
from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from .models import Supportstaff , Staffpayments , ExpenseRecord , Fees , Bankdetails , Receipts , Supportstaffpayment , Teacherspayment , Teachers

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
    return render(request,'finance/expenses/financeaddExpenses.html')

def financeexpensesList(request):
    return render(request,'finance/expenses/financeexpensesList.html')
# expenses views

def financeReports(request):
    return render(request, 'finance/financeReports.html')

def financeStatistics(request):
    return render(request, 'finance/financeStatistics.html')








