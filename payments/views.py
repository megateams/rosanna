from django.shortcuts import render, HttpResponse , redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.db.models import Sum
from django.db.models import Max
from frontend.models import *
from finance.models import *
from django.http import Http404
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse
from django.db.models.functions import ExtractMonth
from django.db import transaction
import openpyxl
from datetime import date 
from datetime import datetime 
from collections import defaultdict
from django.contrib.auth import authenticate, login
from django.db.models import OuterRef, Subquery
from django.db.models import F
from frontend.views import encryptpassword
from finance.views import *

# Create your views here.
def paymentslogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        administrator = Administrators.objects.get(role = 'Payments')

        if administrator.username == username and administrator.password == str(encryptpassword(password)):
            request.session['admin_id'] = administrator.id
            messages.success(request , "Login Successfull")
            return redirect("Payments Dashboard")
        else:
            messages.warning(request, 'Login Failed')
            return redirect('paymentsloginpage')
    return render(request , 'payments/login.html')

def paymentsdashboard(request):
    # Check if the bursar is authenticated (if you are using sessions)
    if 'admin_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('paymentsloginpage')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    admin_id = request.session['admin_id']

    term_data = Term.objects.get(status=1)
    terms = Term.objects.all()

    administrator = Administrators.objects.get(id=admin_id)
   
    utilities = Utilities.objects.filter(term=term_data.current_term, year=term_data.current_year)
    total_amount_paid = utilities.aggregate(Sum('amountpaid'))['amountpaid__sum']
    if total_amount_paid == None:
        total_amount_paid = 0

    supplementary = Supplementaryincome.objects.filter(term=term_data.current_term, year=term_data.current_year)
    total_amt = supplementary.aggregate(Sum('amount'))['amount__sum']
    if total_amt == None:
        total_amt = 0

    fees = Fees.objects.filter(term=term_data.current_term, year=term_data.current_year)
    total_amount = fees.aggregate(Sum('amount'))['amount__sum']
    if total_amount == None:
        total_amount = 0
        
    sspayments = Supportstaffpayment.objects.filter(term=term_data.current_term, year=term_data.current_year)
    total_sspayments = sspayments.aggregate(Sum('amountpaid'))['amountpaid__sum']
    if total_sspayments == None:
        total_sspayments = 0

    trpayments = Teacherspayment.objects.filter(term=term_data.current_term, year=term_data.current_year)
    total_trpayments = trpayments.aggregate(Sum('amountpaid'))['amountpaid__sum']
    if total_trpayments == None:
        total_trpayments = 0

     # Calculate total income (fees)
    total_income = total_amount + total_amt

    # Calculate total expenses (teacher payments + support staff payments + utilities)
    total_expenses = total_trpayments + total_sspayments + total_amount_paid

    # Calculate profit
    profit = total_income - total_expenses

    total = total_amount + total_amount_paid + total_sspayments + total_trpayments
    if total == 0:
        fees_percentage = 0
        utilities_percentage = 0
        sspayments_percentage = 0
        trpayments_percentage = 0
    else:
        fees_percentage = (total_amount / total) * 100
        utilities_percentage = (total_amount_paid / total) * 100
        sspayments_percentage = (total_sspayments / total) * 100
        trpayments_percentage = (total_trpayments / total) * 100

    context = {
        'total_amount_paid': total_amount_paid,
        'total_amount': total_amount,
        'total_amt': total_amt,
        'total_sspayments' : total_sspayments,
        'total_trpayments' : total_trpayments,
        'fees_percentage': fees_percentage,
        'utilities_percentage': utilities_percentage,
        'sspayments_percentage': sspayments_percentage,
        'trpayments_percentage': trpayments_percentage,
        'total_income' : total_income,
        'total_expenses' : total_expenses,
        'profit' : profit,
        'term_data' : term_data,
        'administrator' : administrator,
        'terms' : terms,
    }
    return render(request, "payments/paymentsdashboard.html", context)  

# @login_required

def administrator_profile(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Query the Administrators model to get the Bursar administrator
        try:
            administrator = Administrators.objects.get(role='Payments')
        except Administrators.DoesNotExist:
            # Handle the case where there is no Bursar in the database
            raise Http404("Administrator profile not found")
        
        context = {
            'administrator': administrator,
        }

        return render(request, 'payments/profile.html', context)
    else:
        # Handle the case where the user is not authenticated
        # You can redirect or show an error message here
        # Redirect to the login page or display an error message
        return redirect('administrator_profile')

def edit_administrator_profile(request):
    try:
        # Retrieve the Bursar's data based on their role
        administrator = Administrators.objects.get(role='Payments')
    except Administrators.DoesNotExist:
        raise Http404("Administrator profile not found")

    if request.method == 'POST':
        username = request.POST.get("username")
        new_pass = request.POST.get("new_password")
        confirm_pass = request.POST.get("confirm_password")

        if new_pass == confirm_pass:
            # Update the Bursar's password (replace this with your actual password update logic)
            administrator.password = encryptpassword(new_pass)
            administrator.username = username
            administrator.save()

            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Passwords do not match")

        return redirect("administrator_profile")

    return render(request, 'payments/profile.html', {'administrator': administrator})


# teacherpayments views
def financeaddTeacherpayments(request):
    if 'admin_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('paymentsloginpage')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    admin_id = request.session['admin_id']

    administrator = Administrators.objects.get(id=admin_id)
    teachersdata = Teachers.objects.all()

    if request.method == 'POST':
        teacherid = request.POST.get('teacherid')
        term_data = Term.objects.get(status=1)

        # Capture the current date
        current_date = date.today()

        teacher = Teachers.objects.get(teacherid=teacherid)
        teachername = teacher.teachernames
        # paymentdate = request.POST.get('paymentdate')
        salary = float(teacher.salary)
        amountpaid = float(request.POST.get('amount'))
        term = term_data.current_term
        year = term_data.current_year
        
        if amountpaid > float(teacher.salary):
            messages.error(request , 'Payment not Added')
            return render(request, 'payments/staffpayments/financeaddTeacherpayments.html', {'balancealert':"Amount Paid must not be greater than the Salary" , 'teachers': teachersdata})

        payment = Teacherspayment.objects.filter(teacherid = teacherid).last()

        print(payment.paymentdate)

        if payment == None:
            Teacherspayment.objects.create(
                teacherid = teacherid,
                teachername = teachername,
                paymentdate = current_date,
                salary = salary,
                amountpaid = amountpaid,
                accumulatedpayment = amountpaid,
                balance = float(teacher.salary) - amountpaid,
                term = term,
                year = year
            )

            messages.success(request, 'Teacher payment added successfully.')
            return render(request, 'payments/staffpayments/financeaddTeacherpayments.html', {'teachers': teachersdata, 'administrator': administrator})

        if payment.balance == 0:
            
            if payment.balance == 0 and payment.paymentdate.month == current_date.month and payment.paymentdate.year == current_date.year:
                messages.success(request, 'Teacher already paid for this month.')

            else:
                Teacherspayment.objects.create(
                    teacherid = teacherid,
                    teachername = teachername,
                    paymentdate = current_date,
                    salary = salary,
                    amountpaid = amountpaid,
                    accumulatedpayment = amountpaid,
                    balance = float(teacher.salary) - amountpaid,
                    term = term,
                    year = year
                )
                messages.success(request, 'Payment successfull.')
            return render(request, 'payments/staffpayments/financeaddTeacherpayments.html', {'teachers': teachersdata, 'administrator': administrator})

        if payment.balance > 0:
            accumulatedpayment = payment.accumulatedpayment + amountpaid
            newbalance = payment.salary - accumulatedpayment
            if newbalance < 0:
                messages.error(request , 'Payment not Added')
                return render(request, 'payments/staffpayments/financeaddTeacherpayments.html', {'balancealert':"Amount Paid must not be greater than the Salary" , 'teachers': teachersdata})
            else:
                Teacherspayment.objects.create(
                    teacherid = teacherid,
                    teachername = teachername,
                    paymentdate = current_date,
                    salary = salary,
                    amountpaid = amountpaid,
                    accumulatedpayment = accumulatedpayment,
                    balance = newbalance,
                    term = term,
                    year = year
                )
                messages.success(request, 'Teacher payment added successfully.')
                return render(request, 'payments/staffpayments/financeaddTeacherpayments.html', {'teachers': teachersdata,'administrator': administrator})

    return render(request, 'payments/staffpayments/financeaddTeacherpayments.html', {'teachers': teachersdata,'administrator':administrator})

def financeteacherpaymentsList(request):
    if 'admin_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('paymentsloginpage')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    admin_id = request.session['admin_id']
    term_data = Term.objects.get(status=1)

    administrator = Administrators.objects.get(id=admin_id)
    total_trpayments = Teacherspayment.objects.filter(term=term_data.current_term, year=term_data.current_year).aggregate(Sum('amountpaid'))['amountpaid__sum']
    teacherspayment = Teacherspayment.objects.filter(term=term_data.current_term, year=term_data.current_year)
    context = {
       'teachers':teacherspayment,
       'total_trpayments': total_trpayments, 
       'administrator': administrator
    }
    return render(request,'payments/staffpayments/financeteacherpaymentsList.html' ,context)
# teacherpayments views  

# supportstaffpayments views
def financeaddsupportstaffpayments(request):
    if 'admin_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('paymentsloginpage')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    admin_id = request.session['admin_id']

    administrator = Administrators.objects.get(id=admin_id)
    supportstaffdata = Supportstaff.objects.all()
    
    if request.method == 'POST':
        term_data = Term.objects.get(status=1)
        supportstaffid = request.POST.get('support-staffid')
        supportstaffname = Supportstaff.objects.get(supportstaffid = supportstaffid)
        staffnames = supportstaffname.supportstaffnames
        # paymentdate = request.POST.get('paymentdate')
        salary = float(request.POST.get('salary'))
        amountpaid = float(request.POST.get('amountpaid'))
        term = term_data.current_term
        year = term_data.current_year

        # Capture the current date
        current_date = date.today()


        if amountpaid > float(supportstaffname.salary):
            messages.error(request , 'Payment not Added')
            return render(request, 'payments/staffpayments/financeaddsupportstaffpayments.html', {'balancealert':"Amount Paid must not be greater than the Salary" , 'supportstaff': supportstaffdata, 'administrator': administrator})

        payment = Supportstaffpayment.objects.filter(supportstaffid = supportstaffid).last()

        if payment == None:
            Supportstaffpayment.objects.create(
                supportstaffid = supportstaffid ,
                staffname = staffnames ,
                paymentdate = current_date,
                salary = salary,
                amountpaid = amountpaid,
                accumulatedamount = amountpaid,
                balance = float(supportstaffname.salary) - amountpaid,
                term = term,
                year = year
            )

            messages.success(request, 'Support Staff payment added successfully.')
            return render(request, 'payments/staffpayments/financeaddsupportstaffpayments.html', {'supportstaff': supportstaffdata, 'administrator' :administrator})
        
        if payment.balance == 0:
            Supportstaffpayment.objects.create(
                supportstaffid = supportstaffid ,
                staffname = staffnames ,
                paymentdate = current_date,
                salary = salary,
                amountpaid = amountpaid,
                accumulatedamount = amountpaid,
                balance = float(supportstaffname.salary) - amountpaid,
                term = term,
                year = year
            )

            messages.success(request, 'Support staff payment added successfully.')
            return render(request, 'payments/staffpayments/financeaddsupportstaffpayments.html', {'supportstaff': supportstaffdata, 'administrator':administrator})
        
        if payment.balance > 0:
            accumulatedpayment = payment.accumulatedamount + amountpaid
            newbalance = payment.salary - accumulatedpayment
            if newbalance < 0:
                messages.error(request , 'Payment not Added')
                return render(request, 'payments/staffpayments/financeaddsupportstaffpayments.html', {'balancealert':"Amount Paid must not be greater than the Salary" , 'supportstaff': supportstaffdata})
            else:
                Supportstaffpayment.objects.create(
                    supportstaffid = supportstaffid ,
                    staffname = staffnames ,
                    paymentdate = current_date,
                    salary = salary,
                    amountpaid = amountpaid,
                    accumulatedamount = accumulatedpayment,
                    balance = newbalance,
                    term = term,
                year = year
                )
                messages.success(request, 'Teacher payment added successfully.')
                return render(request, 'payments/staffpayments/financeaddsupportstaffpayments.html', {'teachers': supportstaffdata, 'administrator':administrator})
    return render(request, 'payments/staffpayments/financeaddsupportstaffpayments.html', {'supportstaff': supportstaffdata, 'administrator': administrator})

def financesupportstaffpaymentsList(request):
    if 'admin_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('paymentsloginpage')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    admin_id = request.session['admin_id']
    term_data = Term.objects.get(status=1)

    administrator = Administrators.objects.get(id=admin_id)
    total_sspayments = Supportstaffpayment.objects.filter(term=term_data.current_term, year=term_data.current_year).aggregate(Sum('amountpaid'))['amountpaid__sum']
    support_staff_payments = Supportstaffpayment.objects.filter(term=term_data.current_term, year=term_data.current_year)
    context = {
        'supportstaffpayments': support_staff_payments,
        'total_sspayments': total_sspayments,
        'administrator': administrator
    }

    return render(request, 'payments/staffpayments/financesupportstaffpaymentsList.html', context)

# supportstaffpayments views

def editteacherpayments(request):
    if request.method == 'POST':
        paymentid = request.POST.get('paymentid')
        teacherpayment = Teacherspayment.objects.get(paymentid=paymentid)
        salary = int(request.POST.get('salary'))
        amountpaid = int(request.POST.get('amountpaid'))
        teacherid = request.POST.get('teacherid')
        teachername = request.POST.get('teachername')

        # Calculate the new balance
        balance = salary - amountpaid

        # Fetch all payments made by the teacher
        payments = Teacherspayment.objects.filter(teacherid=teacherid)

        # Initialize accumulated payment with the edited amount paid
        new_accumulatedpayment = amountpaid

        # Calculate the new accumulated payment for all payments
        for payment in payments:
            if payment.paymentid == paymentid:
                # Skip the edited payment
                continue

            # Calculate the new accumulated payment for this payment
            new_accumulatedpayment += payment.amountpaid

        teacherpayment.salary = salary
        teacherpayment.amountpaid = amountpaid
        teacherpayment.balance = balance
        teacherpayment.teacherid = teacherid
        teacherpayment.teachername = teachername

        # Update the accumulated payment
        teacherpayment.accumulatedpayment = new_accumulatedpayment
        teacherpayment.save()

        messages.success(request, "Teacher Payment Edit Successful")
        return redirect('teacherpaymentslists')

    # Rest of your code for GET requests



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
    return render(request , 'payments/staffpayments/editsupportstaffpayments.html' , {'staffpayment': staffpayment})

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

def get_teacher_balance(request , id):
    teacher = Teachers.objects.get(teacherid = id)
    payment = Teacherspayment.objects.get(teacherid = id)
    balance = int(teacher.salary) - int(payment.accumulatedpayment)
    print(balance)
    return JsonResponse({'balance' : balance})

def getsupportstaffbalance(request , id):
    supportstaff = Supportstaff.objects.get(supportstaffid = id)
    payment = Supportstaffpayment.objects.get(supportstaffid = id)
    balance = supportstaff.salary - payment.accumulatedamount
    return JsonResponse({'balance':balance})

def export_teacher_payments_to_excel(request):
    data = Teacherspayment.objects.all().values_list(
        'teacherid', 'teachername', 'paymentdate', 'salary', 'amountpaid', 'balance'
    )

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(['Teacher ID', 'Teacher Name', 'Payment Date', 'Salary', 'Amount Paid', 'Balance'])

    for row_data in data:
        ws.append(row_data)

    # Set column widths
    ws.column_dimensions['A'].width = 15
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15

    filename = 'teacher_payments_data.xlsx'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    wb.save(response)

    return response




def export_support_staff_payments_to_excel(request):
    data = Supportstaffpayment.objects.all().values_list(
        'supportstaffid', 'staffname', 'paymentdate', 'salary', 'amountpaid', 'balance'
    )

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append([
        'Staff ID', 'Staff Name', 'Payment Date', 'Salary', 'Amount Paid', 'Balance'
    ])

    for row_data in data:
        ws.append(row_data)

    # Set column widths
    ws.column_dimensions['A'].width = 15
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15

    filename = 'support_staff_payments.xlsx'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    wb.save(response)

    return response


