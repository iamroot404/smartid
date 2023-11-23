from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from . forms import RegistrationForm, UserForm, UserProfileForm
from . models import Account, UserProfile
from academics.models import AcademicDetails

# from .utils import searchStaff, paginateStaff
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required





# Create your views here.
def login(request):
    if request.method == 'POST':
        registration_number = request.POST['id']
        password = request.POST['password']

        user = auth.authenticate(registration_number=registration_number, password=password, is_active=True)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'You are now logged in.')
            return redirect(request.GET['next'] if 'next' in request.GET  else 'dashboard')
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url= 'login') 
def logout(request):
    auth.logout(request)
    messages.success(request, 'You Are Logged Out!')
    return redirect('login')


@login_required(login_url= 'login')
def addStudent(request):
    
    user = request.user
    if  user.is_admin == True:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone_number = form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                username = email.split("@")[0]
                registration_number = form.cleaned_data['registration_number']
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, username=username, registration_number=registration_number, password=password)
                
                user.save()
    
                
                # messages.success(request, 'Thank you for registering us. We have sent you a verification email to your email address')
                return redirect('view-students')
        else:
            form = RegistrationForm()
        context = {
            'form':form,
        }

        return render(request, 'accounts/add-student.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('dashboard')


@login_required(login_url= 'login')
def viewStudents(request):
    user = request.user
    if  user.is_admin == True:
        students = Account.objects.filter(is_student=True)

        context = {
            'students': students
        }
    
        return render(request, 'accounts/view-students.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('dashboard')

@login_required(login_url= 'login')
def studentProfile(request):
    profile = request.user.userprofile
    userprofile = UserProfile.objects.get(user_id=request.user.id)
    course = AcademicDetails.objects.get(student   =userprofile)
    form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save() 

            return redirect('my-account')
    
    context = {
        'userprofile': userprofile,
        'course': course,
        'form':form
    }
    return render(request, 'accounts/student-profile.html', context)