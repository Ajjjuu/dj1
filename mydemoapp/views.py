from django.shortcuts import render
from django.http import HttpResponse

def greet(request):
    msg="<h1>Hey... <br>You're in my first Django app <br> Warm welcome ;)<h1>"
    return HttpResponse(msg)

