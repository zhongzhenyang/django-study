from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Sequence, Dict
from login import models

# Create your views here.

# user_list: Sequence[Dict[str, str]] = []


def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("Hello World")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        models.UserInfo.objects.create(user=username, pwd=password)
        # user_list.append({"user": username, "pwd": password})
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", context={"user_list": user_list})
