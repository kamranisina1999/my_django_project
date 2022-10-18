from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>hello world</h>')


def main_page(request):
    return HttpResponse('this is main page')
