from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def admin_login(request):
    return HttpResponse(render(request, 'admin_login.html'))

def user_login(request):
    return HttpResponse(render(request, 'user_login.html'))
