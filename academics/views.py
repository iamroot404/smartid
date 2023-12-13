from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AcademicDetailsForm, UnitsForm, RegisterUnits, RegisterUnitsForm
from .models import RegisterUnits, Attendance
from .utils import paginateAttendance, searchAtendance

# Create your views here.
@login_required(login_url= 'login')
def addAcademics(request):
    user = request.user
    if  user.is_admin == True:
        profile = request.user
        form = AcademicDetailsForm(request.POST)
        if request.method =='POST':
                # form = StockForm(request.POST)
                if form.is_valid():
                    dep =  form.save(commit=False)
                    
                    

                    
                    dep.save()
                    # messages.success(request, 'Stock was added successfully!')    
                    return redirect('add-academic-data')
        context = {'form': form}
        return render(request, 'academics/academic-data.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')


@login_required(login_url= 'login')
def addUnits(request):
    user = request.user
    if  user.is_admin == True:
        profile = request.user
        form = UnitsForm(request.POST)
        if request.method =='POST':
                # form = StockForm(request.POST)
                if form.is_valid():
                    dep =  form.save(commit=False)
                    
                    

                    
                    dep.save()
                    # messages.success(request, 'Stock was added successfully!')    
                    return redirect('add-units')
        context = {'form': form}
        return render(request, 'academics/add-units.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')


@login_required(login_url= 'login')
def registerUnits(request):
    user = request.user
    if  user.is_student == True:
        profile = request.user.userprofile
        form = RegisterUnitsForm(request.POST)
        if request.method =='POST':
                # form = StockForm(request.POST)
                
                
                if form.is_valid():


                    
                    dep =  form.save(commit=False)
                    dep.student = profile

                    # units = RegisterUnits.objects.get(unit_id=dep.unit_id, student=profile)
                    # print(units)
                    # if units:
                    #     messages.error(request, 'Unit was already added!')
                    # else:


                    
                    dep.save()
                    # messages.error(request, 'Unit was already added!')    
                    return redirect('my-units')
        context = {'form': form}
        return render(request, 'academics/register-units.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')


@login_required(login_url= 'login')
def myUnits(request):
    user = request.user
    if  user.is_student == True:
        profile = request.user.userprofile
        units = RegisterUnits.objects.filter(student=profile)
    
        context = {'units': units}
        return render(request, 'academics/my-units.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')



def attendance(request):
   if request.method == 'POST':
        registration_number = request.POST['reg']
        unit_code = request.POST['code']

        units = RegisterUnits.objects.get(unit_id__unit_code=unit_code, student__registration_number=registration_number)

        if units:
            att = Attendance.objects.create(unit_id=units)
            att.save()
            messages.success(request, 'Attendance was added successfully!') 
            print("unit found")
        else:
            print("unit not found")
            # messages.error(request, 'Invalid!')
            return redirect('attendance')
    
   return render(request, 'academics/attendance.html')



@login_required(login_url= 'login') 
def myAttendance(request):
    user = request.user
    if  user.is_student == True:
        profile = request.user.userprofile

        attendance = Attendance.objects.filter(unit_id__student=profile)


        context = {'attendance': attendance}
        return render(request, 'academics/my-attendance.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')


@login_required(login_url= 'login')
def viewAttendance(request):
    user = request.user
    if  user.is_admin == True:
       
        attendance, search_query = searchAtendance(request)
        custom_range, attendance = paginateAttendance(request, attendance, 10)
    
        context = {
            'attendance': attendance,
            'search_query': search_query, 
            'custom_range': custom_range
                   }
        return render(request, 'academics/view-attendance.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')