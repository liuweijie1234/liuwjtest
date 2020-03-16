# -*- coding: utf-8 -*-
import time

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from moments.models import WeChatUser, Status, Reply
from django.conf import settings
from blueapps.account.models import User
from django.contrib.auth.decorators import login_required
# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt

def home(request):
    return render(request, 'homepage.html')

@login_required
def show_user(request):
    user = WeChatUser.objects.get(user=request.user)
    return render(request, 'user.html', {"user": user})

@login_required
def show_status(request):
    statuses = Status.objects.all()
    return render(request, 'status.html', {"statuses": statuses})

@login_required
def show_post(request):
    user = WeChatUser.objects.get(user=request.user)
    text = request.POST.get("text")
    uploaded_file = request.FILES.get("pic")

    if uploaded_file:
        file_name = uploaded_file.name
        with open("./moments/static/image/{}".format(file_name), 'wb') as file_handler:
            for block in uploaded_file.chunks():
                file_handler.write(block)
    else:
        file_name = ""

    if text:
        status = Status(user=user, text=text, pics=file_name)
        status.save()
        return redirect("/status")

    return render(request, 'my_post.html')

def register(request):
    try:
        username, password, email = [request.POST.get(key) for key in ("username", "password", "email")]
        user = WeChatUser(user=username, email=email)
        user.set_password(password)
        user.save()

        WeChatUser.objects.create(user=request.user, email=email)
    except Exception as err:
        result = False
        message = str(err)
    else:
        result = True
        message = "Register success"
    return JsonResponse({'result': result, 'message': message})

def update_user(request):
    try:
        kwargs = {key: request.POST.get(key) for key in ('pic', 'region', 'motto', 'email') if request.POST.get(key)}
        WeChatUser.objects.filter(user=request.user).update(**kwargs)

        result = True
        message = "update success"
    except Exception as err:
        result = False
        message = str(err)

    return JsonResponse({"result": result, "message": message})

@login_required
def like(request):
    user = request.user.username
    status_id = request.POST.get("status_id")

    like = Reply.objects.filter(author=user, status=status_id, type="0")
    if like:
        like.delete()
    else:
        Reply.objects.create(author=user, status=Status.objects.get(id=status_id), type="0")
    return JsonResponse({"result": True})


def into_test(request):
    time.sleep(20)
    return JsonResponse({'result': True})
