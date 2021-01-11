from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)   # <WSGIRequest: GET '/news/'>
    # print(dir(request))
    return HttpResponse('Hello World!')


def test(request):
    print(request)   # <WSGIRequest: GET '/news/'>
    # print(dir(request))
    return HttpResponse('<h1>Тестовая страница</h1>')