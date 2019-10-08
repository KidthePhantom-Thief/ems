from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from dangdangapp.models import TBook, DCategory


# Create your views here.

def index(request):
    status = request.session.get('username')
    if not status:
        status = 0

    book = TBook.objects.filter()
    book2 = TBook.objects.filter().order_by('-shelves_date')[:8]
    book3 = TBook.objects.filter().order_by('-shelves_date', '-sales')[:5]
    book4 = TBook.objects.filter().order_by('-book_price')[:8]

    dca = DCategory.objects.filter()

    return render(request, 'dangdangapp/index.html', {
        'book': book,
        'book2': book2,
        'book3': book3,
        'book4': book4,
        'dca': dca,
        'status': status})


def sort(request):
    id = request.GET.get('id')
    way = request.GET.get('way')
    category_id = request.GET.get('category_id')
    return HttpResponse('12345678')


def book_list(request):
    status = request.session.get('username')
    if not status:
        status = 0
    num = request.GET.get('id')
    category_id = request.GET.get('category_id')

    dca = DCategory.objects.filter()


    child_name = 0
    parent_name = 0
    if category_id:
        child_id = category_id
        parent_id = category_id
    else:
        child_id = 0
        parent_id = 0

    if category_id:

        # 有pid的
        if DCategory.objects.get(category_id=category_id).category_pid:
            book = TBook.objects.filter(book_category=category_id)
            child_name = DCategory.objects.get(category_id=category_id).category_name

            parent_id = DCategory.objects.get(category_id=category_id).category_pid

            parent_name = DCategory.objects.get(category_id=parent_id).category_name

        # 没有pid的 大类
        else:
            parent_name = DCategory.objects.get(category_id=category_id).category_name

            l = []
            cate = DCategory.objects.filter(category_pid=category_id)
            for i in cate:
                l.append(i.category_id)
            book = TBook.objects.filter(book_category__in=tuple(l))
    else:
        book = TBook.objects.filter()

    pagntor = Paginator(book, per_page=4)
    # if num>pagntor.num_pages:
    #     pa
    if num:
        # if num <= pagntor.num_pages:
        page = pagntor.page(int(num))
    # else:
    #     page = pagntor.page(pagntor.num_pages)
    else:
        page = pagntor.page(1)
    a = '0:6'
    if page.number >= 5:
        a = str(page.number - 4) + ':' + str(page.number + 3)

    return render(request, 'dangdangapp/booklist.html', {
        'page': page,
        'dca': dca,
        'a': a,
        'child_name': child_name,
        'parent_name': parent_name,
        'parent_id': parent_id,
        'child_id': child_id,
        'status': status,

    })


def book_details(request):
    book_name = request.GET.get('name')
    status = request.session.get('username')
    # book_name = '王道·课件.单人速写'
    if not status:
        status = 0
    book = TBook.objects.filter(book_name=book_name)[0]

    if book:
        return render(request, 'dangdangapp/Book details.html', {
            'book': book,
            'status': status})
    return redirect('dangdangapp:index')
