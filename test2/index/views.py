from django.shortcuts import render, redirect
from . import models


# Create your views here.
def login(request):
    if request.method == "POST":
        us = request.POST.get("username")
        pd = request.POST.get("password")
        try:
            user = models.User.objects.get(username=us)
        except Exception:
            message = "账号不存在"
            return render(request, "source/login.html",  {'message':message})

        if user.password == pd:
            request.session['id_login'] = True
            request.session['username'] = us
            request.session['id_user'] = user.id
            return redirect('/api/course/index/')

        else:
            message = "密码不正确"
            return render(request, "source/login.html", {'message': message})


    return render(request, "source/login.html")




def logout(request):
    request.session.flush()
    return redirect('/api/course/index/')

def register(request):
    return render(request, "source/register.html")
def index(request):
    if not request.session.get('id_login'):
        data = None
        return render(request, "source/index.html", {data: 'data'})
    return render(request, "source/index.html",  {1: 'data'})