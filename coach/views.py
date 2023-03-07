from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def naveen(request):
    return HttpResponse('hi hello')
def karthi(request):
    return HttpResponse('<h1>Mr. IPL is Suresh Raina<h1>')
