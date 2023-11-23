from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DepartmentForm, CourseForm
from .models import Department, Course
from academics.models import AcademicDetails

# Create your views here.
def addDepartment(request):
    user = request.user
    if  user.is_admin == True:
        profile = request.user
        form = DepartmentForm(request.POST)
        if request.method =='POST':
                # form = StockForm(request.POST)
                if form.is_valid():
                    dep =  form.save(commit=False)
                    
                    
 
                    
                    dep.save()
                    # messages.success(request, 'Stock was added successfully!')    
                    return redirect('add-department')
        context = {'form': form}
        return render(request, 'department/add-department.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')

def addCourse(request): 
    user = request.user
    if  user.is_admin == True:
        profile = request.user
        form = CourseForm(request.POST)
        if request.method =='POST':
                # form = StockForm(request.POST)
                if form.is_valid():
                    course =  form.save(commit=False)
                    
                    

                    
                    course.save()
                    # messages.success(request, 'Stock was added successfully!')    
                    return redirect('add-course')
        context = {'form': form}
        return render(request, 'department/add-course.html', context)

    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')
    
def viewDepartment(request):
    user = request.user
    if  user.is_admin == True:
        dep = Department.objects.all()
        

        context = {
            'dep': dep,
           
        }
        return render(request, 'department/view-department.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')

def addCourse(request): 
    user = request.user
    if  user.is_admin == True:
        profile = request.user
        form = CourseForm(request.POST)
        if request.method =='POST':
                # form = StockForm(request.POST)
                if form.is_valid():
                    course =  form.save(commit=False)
                    
                    

                    
                    course.save()
                    # messages.success(request, 'Stock was added successfully!')    
                    return redirect('add-course')
        context = {'form': form}
        return render(request, 'department/add-course.html', context)

    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')
    
def viewCourse(request):
    user = request.user
    if  user.is_admin == True:
        course = Course.objects.all()
        

        context = {
            'course': course,
           
        }
        return render(request, 'department/view-course.html', context)
    else:
        messages.error(request, "Access Route Denied!")
        return redirect('my-account')