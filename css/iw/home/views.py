from django.shortcuts import render
from django.http import HttpResponse


def hello_main(request):
    hello_string = "hello world"
    return HttpResponse(hello_string)


def hello_about(request):
    hello_about = "i am suraj kumar sah"
    return HttpResponse(hello_about)
