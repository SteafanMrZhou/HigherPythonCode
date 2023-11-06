from .models import HpUser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import concurrent.futures


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        user = HpUser()
        user.username = username
        user.password = password
        user.sex = sex
        user.save()
        return HttpResponse("注册成功")


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        currUser = HpUser.objects.filter(username=username, password=password)
        if currUser:
            return HttpResponse("登录成功")
        return HttpResponse("登录失败")


# 高并发环境实现
# @csrf_exempt
# def register(request):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         if request.method == "POST":
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             sex = request.POST.get('sex')
#             user = HpUser()
#             user.username = username
#             user.password = password
#             user.sex = sex
#             future = executor.submit(user.save())
#             print(future)
#             return HttpResponse("注册成功")

# @csrf_exempt
# def login(request):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         if request.method == "POST":
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             currUserfuture = executor.submit(HpUser.objects.filter(username=username, password=password))
#             if currUserfuture:
#                 print(currUserfuture)
#                 return HttpResponse("登录成功")
#             return HttpResponse("登录失败")


