from django.shortcuts import render
from myli.models import Hu1
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def chaxun(request):
    ls = Hu1.objects.filter(dz__contains='香杨路120')[:10]
    return render(request, "cx1.html", locals())
def tjcx(request):
    if(request.POST):
        ls = Hu1.objects.filter(dz__contains = request.POST['tj'])[:15]
    return render(request, "tjcx.html", locals())
def login1(request):
    if request.POST:
        ls = request.POST['u'] + '  ' +  request.POST['p']
        return HttpResponse("<h1>" + ls + "</h1>")
    else:
        return render(request, "Login.html")

def temn(request):
    return render(request,"temn.html")

def demo(request):
    return  render(request,"pop.html")



def index(request):
    if (request.POST):
        ls = Hu1.objects.filter(dz__contains=request.POST['tj'])[:15]
    return render(request, "sf.html", locals())

@csrf_exempt
def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('确认密码不能为空')
        else:
            password2 = request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append('邮箱不能为空')
        else:
            email = request.POST.get('email')

        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('两次输入密码不一致')

        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag :
            user = User.objects.create_user(account,email,password)
            user.save()

            userlogin = auth.authenticate(username = account,password = password)
            auth.login(request,userlogin)
            return HttpResponse("<h1>"+request.POST['account']+"register su </h1>")

    return render(request,'reg.html', {'errors': errors})


# 用户登录
@csrf_exempt
def my_login(request):
    errors =[]
    account = None
    password = None
    if request.method == "POST":
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')

        if account is not None and password is not None:
            user = auth.authenticate(username=account,password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return render(request,'sf.html',locals())
                else:
                    errors.append('用户名错误')
            else:
                errors.append('用户名或密码错误')
    return render(request,'Login.html', {'errors': errors})

# 用户退出
def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('sf')