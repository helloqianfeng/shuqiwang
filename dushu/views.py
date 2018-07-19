from books.models import Book
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
# http://127.0.0.1:8000/book?num=
def home(request):
    num = request.GET.get('num')
    print(num)
    booklist = Book.objects.all().order_by('count')
    # from django.core import serializers
    # booklist_json = serializers.serialize("json", booklist)
    paginator = Paginator(booklist, 20)
    page = paginator.page(int(num))

    # from django.core import serializers
    # page_json = serializers.serialize("json", page)
    # print(page_json)
    # print(type(page_json))

    # return JsonResponse({'current_page':num,
    #                      'books':page_json,
    #                      'page_range':tuple(paginator.page_range)})
    return render(request, 'home.html',
                  {'current_page': num,
                   'books': page.object_list,
                   'page_range': paginator.page_range})


# http://127.0.0.1:8000/book/?cate= & state= & property= & size= & quality= & refresh_date=

def serch(request, num=1,
          cate=None,
          state=None,
          property=None, size=None, quality=None, refresh_date=None):

    wheres = {}
    if cate: wheres['cate'] = cate
    if state: wheres['state'] = state
    if property: wheres['property'] = property
    if size: wheres['size'] = size
    if quality: wheres['quality'] = quality
    if refresh_date: wheres['refresh_date'] = refresh_date

    booklist = Book.objects.filter(**wheres).order_by('count').all()
    paginator = Paginator(booklist, 20)
    page = paginator.page(int(num))
    print(type(paginator.page_range))
    return JsonResponse({'current_page': num,
                         'books': page.object_list,
                         'page_range': paginator.page_range})
