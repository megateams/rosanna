from django.shortcuts import render, redirect
from django.contrib import messages
from frontend.models import Teachers

# Create your views here.

# view for the login page
def login(request):
    return render(request, 'teacher/login.html')

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Query the database for a teacher with matching username or email
        try:
            teacher = Teachers.objects.get(username=username)
        except Teachers.DoesNotExist:
            try:
                teacher = Teachers.objects.get(email=username)
            except Teachers.DoesNotExist:
                teacher = None

        if teacher and teacher.password == password:
            # If the credentials are valid, redirect to the teacher dashboard
            request.session['teacher_id'] = teacher.teacherid  # Save the teacher's ID in the session
            return redirect('Teacher Dashboard')  # Replace 'dashboard' with the name/url of your teacher dashboard view

        else:
            # If the credentials are invalid, display an error message
            messages.error(request, 'Invalid username/email or password.')
            return redirect('Login Page')
    

def logout_view(request):
    # Clear session data
    request.session.clear()

    # Add a success message to inform the user about the successful logout
    messages.success(request, 'You have been logged out.')

    # Redirect to the login page
    return redirect('Login Page')

def dashboard(request):
    # Check if the teacher is authenticated (if you are using sessions)
    if 'teacher_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('Login Page')  # Replace 'login' with the name/url of your login view

    # Get the teacher ID from the session
    teacher_id = request.session['teacher_id']

    # Query the database to get the teacher's information
    try:
        teacher = Teachers.objects.get(teacherid=teacher_id)
    except Teachers.DoesNotExist:
        teacher = None
    return render(request, 'teacher/dashboard.html',{'teacher': teacher})

def profile(request,teacher_id):
    teachers = Teachers.objects.get(teacherid = teacher_id)
    return render(request, 'teacher/profile.html', {'teacher': teachers})    

def paymenthistory(request):
    return render(request, 'teacher/paymenthistory.html')   