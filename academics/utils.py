from django.db.models import Q
from .models import Stock
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
 

def paginateStock(request, stock, results):
    page = request.GET.get('page')
    paginator = Paginator(stock, results)

    try:
        stock = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        stock = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        stock = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    return custom_range, stock

def searchStock(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

  

    stock = Stock.objects.distinct().filter(
        Q(stock_id__icontains=search_query) | 
        Q(batch_number__icontains=search_query) |
        Q(stock_name__icontains=search_query) |
        Q(expiry__icontains=search_query)
    )


    return stock, search_query