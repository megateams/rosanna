
from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.db.models import Sum
from frontend.models import *
from django.core import serializers
from django.http import JsonResponse
# from django_excel_response import ExcelResponse
from django.db.models.functions import ExtractMonth
import openpyxl

def editteacherpayments(request):
    if request.method == 'POST':
        paymentid = request.POST.get('paymentid')
        teacherpayment = Teacherspayment.objects.get(paymentid = paymentid)
        salary = request.POST.get('salary')
        amountpaid = request.POST.get('amountpaid')
        balance = int(salary) - int(amountpaid)
        teacherid = request.POST.get('teacherid')
        teachername = request.POST.get('teachername')

        teacherpayment.salary = salary 
        teacherpayment.amountpaid = amountpaid 
        teacherpayment.balance = balance 
        teacherpayment.teacherid = teacherid 
        teacherpayment.teachername = teachername 

        teacherpayment.save()
        messages.success(request , "Teacher Payment Edit Successfull")

        return redirect('teacherpaymentslists')

    return render(request , 'finance/staffpayments/editteacherpayments.html' , {'teacherpayment' : teacherpayment})

def editsupportstaffpayment(request):
    if request.method == 'POST':
        paymentid = request.POST.get('paymentid')
        staffpayment = Supportstaffpayment.objects.get(paymentid = paymentid)
        supportstaffid = request.POST.get('supportstaffid')
        salary = request.POST.get('salary')
        amountpaid = request.POST.get('amountpaid')
        #balance = request.POST.get('balance')
        #paymentmethod = request.POST.get('paymentmethod')
        #bankaccnum = request.POST.get('bankaccnum')
        paymentdate = request.POST.get('paymentdate')
        staffname = request.POST.get('staffname')

        staffpayment.supportstaffid = supportstaffid
        staffpayment.salary = salary
        staffpayment.amountpaid = amountpaid 
        staffpayment.balance = int(salary) - int(amountpaid)
        #staffpayment.paymentmethod = paymentmethod
        #staffpayment.bankaccnum = bankaccnum
        staffpayment.paymentdate = paymentdate 
        staffpayment.staffname = staffname 

        staffpayment.save

        messages.success(request , 'Edited Successfully')
        return redirect('SupportstaffpaymentsLists')
    return render(request , 'finance/staffpayments/editsupportstaffpayments.html' , {'staffpayment': staffpayment})

def deleteteacherpayment(request):
    if request.method == 'POST':
        paymentid = request.POST.get('paymentid')
        payid = Teacherspayment.objects.filter(paymentid = paymentid)
        payid.delete()
        messages.success(request , 'Payment Deleted Successfully')
        return redirect('teacherpaymentslists')

def deletesupportstaffpayment(request):
    if request.method == 'POST':
        paymentid = request.POST.get('paymentid')
        payid = Supportstaffpayment.objects.filter(paymentid = paymentid)
        payid.delete()
        messages.success(request , "Payment deleted successfully")
        supportstaffinfo = Supportstaffpayment.objects.all()
        return redirect('SupportstaffpaymentsLists')

def financeaddStaffpayments(request):
    if request.method == 'POST':
        supportstaffid = request.POST.get('support-staffid')
        supportstaffname = request.POST.get('support-staffname')
        paymentdate = request.POST.get('datepaid')
        salary = request.POST.get('salary')
        amount = request.POST.get('amount')

        Supportstaffpayment.objects.create(
            supportstaffid = supportstaffid ,
            salary = salary ,
            amountpaid = amount ,
            #balance = balance ,
            supportstaffname = supportstaffname,
            #paymentdate = datepaid,
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



# def financedashboard(request):
#     # Extract distinct months for each payment kind
#     trpayments_months = Teacherspayment.objects.dates('paymentdate', 'month', order='ASC').distinct()
#     sspayments_months = Supportstaffpayment.objects.dates('paymentdate', 'month', order='ASC').distinct()
#     fees_months = Fees.objects.dates('date', 'month', order='ASC').distinct()
#     expenses_months = ExpenseRecord.objects.dates('expensedate', 'month', order='ASC').distinct()

#     # Extract expense data
#     expenses_by_month = ExpenseRecord.objects.annotate(month=ExtractMonth('expensedate')).values('month').annotate(total_amount_paid=Sum('amountpaid')).order_by('month')

#     # Extract and aggregate data for each payment kind per month
#     fees_by_month = Fees.objects.annotate(month=ExtractMonth('date')).values('month').annotate(total_amount=Sum('amount')).order_by('month')

#     # Extract support staff payment data
#     sspayments_by_month = Supportstaffpayment.objects.annotate(month=ExtractMonth('paymentdate')).values('month').annotate(total_sspayments=Sum('amountpaid')).order_by('month')

#     # Extract teacher payment data
#     trpayments_by_month = Teacherspayment.objects.annotate(month=ExtractMonth('paymentdate')).values('month').annotate(total_trpayments=Sum('amountpaid')).order_by('month')

  

#     months = ["February", "March", "April", "May"]
#     payments_total = [entry['total_trpayments'] for entry in trpayments_by_month]
#     fees_total = [entry['total_amount'] for entry in fees_by_month]
#     expenses_total = [entry['total_amount_paid'] for entry in expenses_by_month]

#     context = {
#         'trpayments_months' : trpayments_months,
#         'fees_months' : trpayments_months,
#         'expenses_months' : expenses_months,
#         'payments_total' : payments_total,
#         'fees_total': fees_total,
#         'expenses_total': expenses_total
#     }
#     return render(request, "finance/financedashboard.html", context)


# Create your views here.
def financedashboard(request):
    
    expenses = ExpenseRecord.objects.all()
    total_amount_paid = expenses.aggregate(Sum('amountpaid'))['amountpaid__sum']

    fees = Fees.objects.all()
    total_amount = fees.aggregate(Sum('amount'))['amount__sum']

    sspayments = Supportstaffpayment.objects.all()
    total_sspayments = sspayments.aggregate(Sum('amountpaid'))['amountpaid__sum']

    trpayments = Teacherspayment.objects.all()
    total_trpayments = trpayments.aggregate(Sum('amountpaid'))['amountpaid__sum']

    context = {
        'total_amount_paid': total_amount_paid,
        'total_amount': total_amount,
        'total_sspayments' : total_sspayments,
        'total_trpayments' : total_trpayments,

    }
    return render(request, "finance/financedashboard.html", context)

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
        print(amount)
        print(classfees)

        # Check if the student with the same stdnumber is already added to the fees
        if Fees.objects.filter(stdnumber=stdnumber).exists():
            messages.error(request, 'This student has already been added to fees.')
            students = Student.objects.all()
            fees_structures = Feesstructure.objects.all()
            return render(request, 'finance/fees/financeaddFees.html', {'students': students, 'fees_structures': fees_structures})

        if int(amount) <= int(classfees):
            # Create a new Fees object and save it to the database
            fees = Fees.objects.create(
                stdnumber_id=stdnumber,
                stdname=stdname,
                studentclass=studentclass,
                classfees=classfees,
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
    total_amount = Fees.objects.aggregate(Sum('amount'))['amount__sum']
    fees_list = Fees.objects.all()
    context = {
        'fees_list': fees_list,
        'total_amount': total_amount,
    }
    return render(request,'finance/fees/financefeesList.html',context)

def delete_fee(request):
    if request.method == 'POST':
        paymentid = request.POST.get("paymentid")
        fee = Fees.objects.get(paymentid=paymentid)
        fee.delete()
        messages.success(request, f"Fee record {paymentid} has been deleted.")
        return redirect('Fees List')  # Adjust this to the correct URL name

    return redirect('Fees List')  # Adjust this to the correct URL name
def edit_std_fees(request):
    if request.method == 'POST':
        paymentid = request.POST.get("paymentid")
        amount = float(request.POST.get("amount"))
        modeofpayment = request.POST.get("modeofpayment")
        date = request.POST.get("date")
        fee = Fees.objects.get(paymentid=paymentid)
        classfees = float(fee.classfees)
        balance = classfees - amount

        fee.amount = amount
        fee.balance = balance
        fee.modeofpayment = modeofpayment
        fee.date = date
        fee.save()
        messages.success(request, f"Fee record {paymentid} has been edited.")
        return redirect('Fees List')  # Adjust this to the correct URL name
# fees views

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

# teacherpayments views
def financeaddTeacherpayments(request):
    teachersdata = Teachers.objects.all()
    
    if request.method == 'POST':
        teacherid = request.POST.get('teacherid')
        teachername = Teachers.objects.get(teacherid = teacherid).teachernames
        paymentdate = request.POST.get('paymentdate')
        salary = request.POST.get('salary')
        amountpaid = request.POST.get('amount')
        balance = request.POST.get('balance')
        # paymentmethod = request.POST.get('paymentmethod')
        # bankaccnum = request.POST.get('bankaccnum')
        
        Teacherspayment.objects.create(
            teacherid = teacherid ,
            teachername = teachername ,
            paymentdate = paymentdate ,
            salary = salary ,
            amountpaid = amountpaid ,
            balance = balance ,
            # paymentmethod = paymentmethod ,
            # bankaccnum = bankaccnum ,
        )
        
        Teacherspayment.save
        return redirect('teacherpaymentslists')
        
    return render(request,'finance/staffpayments/financeaddTeacherpayments.html' , {'teachers':teachersdata})

def financeteacherpaymentsList(request):
    total_trpayments = Teacherspayment.objects.aggregate(Sum('amountpaid'))['amountpaid__sum']
    teacherspayment = Teacherspayment.objects.all()
    context = {
       'teachers':teacherspayment,
       'total_trpayments': total_trpayments, 
    }
    return render(request,'finance/staffpayments/financeteacherpaymentsList.html' ,context)
# teacherpayments views

# supportstaffpayments views
def financeaddsupportstaffpayments(request):
    if request.method == 'POST':
        support_staff_id = request.POST.get('support-staffid')
        paymentdate = request.POST.get('paymentdate')
        salary = float(request.POST.get('salary'))
        amount_paid = float(request.POST.get('amountpaid'))
        supportstaffrow = Supportstaff.objects.get(supportstaffid = support_staff_id)
        balance = salary - amount_paid
        # Fetch the support staff payment record
        supportstaffrow = Supportstaff.objects.get(supportstaffid=support_staff_id)

        # Update the payment record with the new amount paid and calculate the 
        payment = Supportstaffpayment.objects.create(
            supportstaffid = support_staff_id,
            amountpaid = amount_paid,
            salary = salary,
            paymentdate = paymentdate,
            balance = balance,
            staffname = supportstaffrow.supportstaffnames
        )
        payment.save()

        return redirect('SupportstaffpaymentsLists')  # Redirect to the list page

    context = {
        'support_staff': Supportstaff.objects.all()
    }
    return render(request, 'finance/staffpayments/financeaddsupportstaffpayments.html', context)

def financesupportstaffpaymentsList(request):
    total_sspayments = Supportstaffpayment.objects.aggregate(Sum('amountpaid'))['amountpaid__sum']
    support_staff_payments = Supportstaffpayment.objects.all()
    context = {
        'supportstaffpayments': support_staff_payments,
        'total_sspayments': total_sspayments,
    }

    return render(request, 'finance/staffpayments/financesupportstaffpaymentsList.html', context)

# supportstaffpayments views

# expenses views
def financeaddExpenses(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        expensedate = request.POST.get('expensedate')
        amountpaid = request.POST.get('amountpaid')
        expense_record = ExpenseRecord(
            category=category,
            expensedate=expensedate,
            amountpaid=amountpaid,
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

def delete_expense(request):
    if request.method == 'POST':
        expenseid = request.POST.get("expenseid")
        try:
            expense = ExpenseRecord.objects.get(expenseid=expenseid)
            expense.delete()
            messages.success(request, f"Expense record {expenseid} has been deleted.")
        except ExpenseRecord.DoesNotExist:
            messages.error(request, f"Expense record {expenseid} does not exist.")

    return redirect('Expenses List')  # Adjust this to the correct URL name


def edit_expense(request, expenseid):
    try:
        expense = ExpenseRecord.objects.get(expenseid=expenseid)

        if request.method == 'POST':
            updated_category = request.POST.get('category')
            updated_expensedate = request.POST.get('expensedate')
            updated_amountpaid = request.POST.get('amountpaid')
            expense.category = updated_category
            expense.expensedate = updated_expensedate
            expense.amountpaid = updated_amountpaid
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

# def financeStatistics(request):
#     return render(request, 'finance/financeStatistics.html')

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

def get_staff_salary(request,id):
    support_staff = Supportstaff.objects.get(pk=id)
    salary = support_staff.salary
    staff_data={
        'salary':salary,
    }
    return JsonResponse(staff_data)

def get_teacher_salary(request , id):
    teacher = Teachers.objects.get(teacherid = id)
    salary = teacher.salary
    teachersalary = {
        'salary' : salary,
    }
    return JsonResponse(teachersalary)

def get_teacher_balance(request , id , amountpaid):
    teacher = Teachers.objects.get(teacherid = id)
    balance = int(teacher.salary) - int(amountpaid)
    return JsonResponse({'balance' : balance})

def export_finance_fees_to_excel(request):
    # Fetch all the data from the Fees model
    data = Fees.objects.all().values_list(
        'paymentid', 'stdnumber__stdnumber', 'stdname', 'studentclass', 'amount', 'balance', 'modeofpayment', 'date'
    )

    # Create a new workbook and add a worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write field names to the worksheet as headers
    ws.append(['Payment ID', 'Student Number', 'Student Name', 'Student Class', 'Amount', 'Balance', 'Mode of Payment', 'Date'])

    # Write data to the worksheet
    for row_data in data:
        ws.append(row_data)

    # Set the column width for the date column
    ws.column_dimensions['A'].width = 15  # Adjust the width as needed
    ws.column_dimensions['B'].width = 15  # Adjust the width as needed
    ws.column_dimensions['C'].width = 15  # Adjust the width as needed
    ws.column_dimensions['D'].width = 15  # Adjust the width as needed
    ws.column_dimensions['E'].width = 15  # Adjust the width as needed
    ws.column_dimensions['F'].width = 15  # Adjust the width as needed
    ws.column_dimensions['H'].width = 15  # Adjust the width as needed

    # Set the filename and content type for the response
    filename = 'finance_fees_data.xlsx'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Save the workbook to the response
    wb.save(response)

    return response


def export_fees_structure_to_excel(request):
    data = Feesstructure.objects.all().values_list(
        'classname', 'amount'
    )

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(['Class', 'Amount'])

    for row_data in data:
        ws.append(row_data)

    # Set the column width for the amount column
    ws.column_dimensions['A'].width = 15

    filename = 'fees_structuredata.xlsx'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    wb.save(response)

    return response

def export_expenses_to_excel(request):
    data = ExpenseRecord.objects.all().values_list(
        'expenseid', 'category', 'expensedate', 'amountpaid'
    )

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(['Expense ID', 'Category', 'Expense Date', 'Amount Paid'])

    for row_data in data:
        ws.append(row_data)

    ws.column_dimensions['A'].width = 15
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15

    filename = 'expenses_data.xlsx'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    wb.save(response)

    return response
















