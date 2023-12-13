from django.db.models import Q
from .models import Account
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
 

def paginateStudents(request, students, results):
    page = request.GET.get('page')
    paginator = Paginator(students, results)

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        students = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        students = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    return custom_range, students

def searchStudents(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

  

    students = Account.objects.distinct().filter(
        Q(registration_number__icontains=search_query) | 
        Q(first_name__icontains=search_query) | 
        Q(last_name__icontains=search_query) |
        Q(phone_number__icontains=search_query)
    ).exclude(is_lecturer=True, is_admin=True, is_superadmin=True)


    return students, search_query