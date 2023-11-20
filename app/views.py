from django.shortcuts import render

# Create your views here.

def auro(request):
    return render(request,'auro.html')

def kalu(request):
    return render(request,'kalu.html')