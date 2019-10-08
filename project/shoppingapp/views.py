import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from shoppingapp.models import TUser, TShoppingCart, TBook


class Cart_items():
    def __init__(self, book, count):
        # book是从数据库书籍详情表中查出来的model对象
        self.book = book
        self.count = count
        self.cost = book.book_dprice * self.count


class Cart():
    def __init__(self):
        self.total_price = 0
        self.save_price = 0
        # 列表存放的是Car_items对象
        self.cart_items = []
        self.del_items = []

    # 计算总价
    def sums(self):
        self.total_price = 0
        self.save_price = 0
        print(self.cart_items)
        for i in self.cart_items:
            self.total_price += i.book.book_dprice * i.count
            self.save_price += (i.book.book_price - i.book.book_dprice) * i.count

    # 增加商品
    def add_car(self, book_id, num):
        book_id = int(book_id)
        for i in self.cart_items:

            if i.book.book_id == book_id:
                i.count += num
                print(i.count)
                self.sums()
                return
        print(self.cart_items)
        a = TBook.objects.get(book_id=book_id)

        self.cart_items.append(Cart_items(a, num))

        self.sums()

    # 删除商品
    def del_car(self, book_id1):
        book_id = int(book_id1)
        for i in self.cart_items:
            if i.book.book_id == book_id:
                self.cart_items.remove(i)
                self.del_items.append(TBook.objects.get(book_id=book_id))
                self.sums()

    # 修改商品
    def change_nums(self, book_id, nums):
        for i in self.cart_items:
            if i.book.book_id == book_id:
                print(i.count, type(i.count), 'i.count')
                i.count = nums
                self.sums()

def cart_default(b):
    if isinstance(b,Cart_items):
        pass


def car(request):
    username = request.session.get('username')

    if username:

        cart1 = request.session.get('cart1')

        cart1 = ''
        user_id = TUser.objects.get(user_email=username).user_id
        ls = []
        for i in TShoppingCart.objects.filter(user_id=user_id):

            if cart1:
                cart1.add_car(i.book_id, i.count)

                request.session['cart'] = cart1
            else:
                cart1 = Cart()
                cart1.add_car(i.book_id, i.count)

                request.session['cart1'] = cart1
        return render(request, 'shoppingapp/car.html', {
            'status': username,
            'cart_items': cart1.cart_items,
            'cart': cart1,
            'total_price': cart1.total_price,
            'save_price': cart1.save_price,
        })
    else:
        username = '0'
        cart = request.session.get('cart')
        if not cart:
            cart = Cart()
            request.session['cart'] = cart
        return render(request, 'shoppingapp/car.html', {
            'status': username,
            'cart_items': cart.cart_items,
            'cart': cart,
        })


def add_cart(request):
    try:
        book_id = request.POST.get('book_id')
        buy_num = request.POST.get('buy_num')
        username = request.session.get('username')
        cart = request.session.get('cart')
        cart1 = request.session.get('cart1')
        if username:
            user_id = TUser.objects.get(user_email=username).user_id
            sum1 = TShoppingCart.objects.count()
            TShoppingCart.objects.create(id=str(sum1 + 1), book_id=book_id, count=buy_num, user_id=user_id)

            if cart1:
                cart1.add_car(book_id, 1)
                request.session['cart1'] = cart1
            else:
                cart1 = Cart()
                cart1.add_car(book_id, 1)
                request.session['cart1'] = cart1

        else:
            if cart:
                cart.add_car(book_id)
                request.session['cart'] = cart
            else:
                cart = Cart()
                cart.add_car(book_id, 1)
                request.session['cart'] = cart

        return HttpResponse('1')

    except:
        return HttpResponse('0')


def change_car_cart(request):
    book_id = request.POST.get('a')
    value = request.POST.get('value')

    int_value = int(value)
    int_book_id = int(book_id)
    username = request.session.get('username')
    try:
        if username:
            user_id = TUser.objects.get(user_email=username).user_id
            cart1 = request.session.get('cart1')

            cart1.change_nums(int_book_id, int_value)

            cart_book = TShoppingCart.objects.get(user_id=user_id, book_id=book_id)
            cart_book.count = int_value
            cart_book.save()
            save_money = cart1.save_price

            cost = cart1.total_price

            request.session['cart1'] = cart1
            str1 = '[' + str(cost) + ',' + str(save_money) + ']'

        else:
            cart = request.session.get('cart')
            cart.change_nums(int_book_id, int_value)

            cost = cart.total_price


            request.session['cart'] = cart
            save_money = cart.save_price
            str1 = '[' + str(cost) + ',' + str(save_money) + ']'

        return HttpResponse(str1)
    except:
        return HttpResponse('0')


def del_car_cart(request):
    book_id = request.POST.get('book_id')

    username = request.session.get('username')
    try:
        if username:
            car_cart = TShoppingCart.objects.get(book_id=book_id)
            car_cart.delete()
            cart1 = request.session.get('cart1')
            cart1.del_car(book_id)
            json.dumps(list(cart1),default=cart_default)
            # request.session['cart1'] = cart1

        else:
            cart = request.session.get('cart')
            cart.del_car(book_id)

            request.session['cart'] = cart


        return HttpResponse('1')
    except:
        return HttpResponse('0')


def del_cart(request):

    return HttpResponse('1111111111')
