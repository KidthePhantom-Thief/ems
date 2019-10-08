import hashlib
import random
import re
import string

from django.http import HttpResponse
from django.shortcuts import render, redirect

from templates.userapp.captcha.image import ImageCaptcha
from userapp.models import TBook, DCategory, TUser


# Create your views here.

def hashlib_pwd(txt_password):
    sha256 = hashlib.sha256()
    sha256.update(txt_password.encode())
    res = sha256.hexdigest()
    return res


def create_captcha(request):
    # 创建 验证码图片对象
    img = ImageCaptcha()
    # print(img)

    # 验证码随机验证码库 大小写英文字符 数字
    code_list = random.sample(string.ascii_letters + string.digits, 4)
    # print(code_list)
    random_str = ''.join(code_list)
    # 保存在session中 为以后 验证做准备
    request.session['code1'] = random_str
    # print(random_str)
    data = img.generate(random_str)
    return HttpResponse(data, 'image/png')


def captcha_logic(request):
    str1 = request.session.get('code1')
    str2 = request.POST.get('txt_vcode')
    print(str1, str2)
    if str1.lower() == str2.lower():
        return HttpResponse('1')
    return HttpResponse('0')


def login(request):
    return render(request, 'userapp/login.html')


def login_logic(request):
    username = request.POST.get('txtUsername')
    password = request.POST.get('txtPassword')
    cookie1 = request.POST.getlist('autologin')
    print(cookie1)
    print(username, password)
    res1 = hashlib_pwd(password)
    str1 = TUser.objects.get(user_email=username).user_name
    print(str1)
    hash_password = res1 + str1
    print(hash_password)
    if TUser.objects.filter(user_email=username, user_password=hash_password):
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        request.session['username'] = username
        if cookie1:
            res = HttpResponse('1')
            res.set_cookie('login', username, max_age=7 * 24 * 3600)
            return res
        else:
            return HttpResponse('1')
    return HttpResponse('0')


def check_all(request):
    try:
        txt_username = request.POST.get('txt_username')
        txt_password = request.POST.get('txt_password')

        user_id = TUser.objects.count()
        str1 = ''.join(random.sample(string.printable, 4))
        print(str1)
        new_password = hashlib_pwd(txt_password) + str1
        print(new_password, '新密码')
        print(len(new_password), '新密码')
        print(user_id + 1)
        TUser.objects.create(user_id=user_id + 1, user_email=txt_username, user_password=new_password, user_name=str1)
        print('11111111111111')
        request.session['username'] = txt_username
        return HttpResponse('1')

    except:
        return HttpResponse('0')


def check_username(request):
    username = request.POST.get('username')
    print(username)
    re.findall('', username)
    if TUser.objects.filter(user_email=username):
        print('1111111111111111')
        return HttpResponse('1')
    print('000000000000000000000')
    return HttpResponse('0')


def register(request):
    username = request.POST.get('txt_username')
    password1 = request.POST.get('txt_password')
    return render(request, 'userapp/register.html')


def register_ok(request):
    username = request.session.get('txt_username')
    return render(request, 'userapp/register ok.html', {
        'username': username
    })


def del_login(request):
    print('2222222222222222222222222222222222')
    del request.session['username']
    del request.session['cart']
    # res = redirect('dangdangapp:index')
    # res.set_cookie('login','',max_age=0)
    return redirect('dangdangapp:index')

