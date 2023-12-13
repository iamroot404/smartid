from django.db.models import Q
from .models import Attendance
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
 

def paginateAttendance(request, attendance, results):
    page = request.GET.get('page')
    paginator = Paginator(attendance, results)

    try:
        attendance = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        attendance = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        attendance = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    return custom_range, attendance

def searchAtendance(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

  

    attendance = Attendance.objects.distinct().filter(
        Q(unit_id__unit_id__unit_code__icontains=search_query) | 
       
        Q(unit_id__unit_id__unit_name__icontains=search_query)
    )


    return attendance, search_query