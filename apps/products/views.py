# apps/products/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, "homepage.html")

def fake_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"[DEBUG] 收到帳號: {username}, 密碼: {password}")
        #return HttpResponse(f"登入成功！歡迎 {username}")
    return redirect("function_base")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def inbound(request):
    return render(request, "inbound.html")

@login_required
def outbound(request):
    return render(request, "outbound.html")

@login_required
def function_base(request):
    return render(request, "function_base.html")
