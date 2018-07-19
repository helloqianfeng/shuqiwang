# coding:utf-8
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from hashlib import sha1

# Create your views here.
from dushu.models import UserInfo


def register(request):
    return render(request, '')


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    uphone = post.get('phone')
    uimg = post.get('img1')
    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register')
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    # 存数据
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.uphone = uphone
    user.uimg = uimg
    user.save()
    return redirect('/user/login')


# 判断注册用户是否存在
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


# def login(request):
#     uname = request.COOKIES.get('uname','')
#     context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
#     return render(request,)
def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')

    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            r = HttpResponseRedirect('/user/info/')
            return r
        else:
            return render('', '')
