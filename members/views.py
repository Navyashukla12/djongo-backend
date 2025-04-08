
from django.shortcuts import render
from django.template import loader

def members(request):
    return render(request,'index.html')