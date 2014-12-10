# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

def index(request):
    return render(request,'index.html')

def data(request):
    return render(request,'data.html')

def impressum(request):
    return render(request,'impressum.html')
