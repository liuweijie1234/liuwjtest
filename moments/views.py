# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt

def home(request):
    return render(request, 'homepage.html')

def show_user(request):
    po = {
        "name": "xiao po",
        "motto": "I Love KungFu",
        "email": "po@disney.com",
        "region": "Shanxi",
        "pic": "Po2.jpg"
    }
    return render(request, 'user.html', {"user": po})

def show_status(request):
    return render(request, 'status.html')

def show_post(request):
    return render(request, 'my_post.html')

# def home(request):
#     """
#     首页
#     """
#     return render(request, 'moments/index_home.html')
#
#
# def dev_guide(request):
#     """
#     开发指引
#     """
#     return render(request, 'moments/dev_guide.html')
#
#
# def contact(request):
#     """
#     联系页
#     """
#     return render(request, 'moments/contact.html')
#