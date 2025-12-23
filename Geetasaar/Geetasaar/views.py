from django.shortcuts import HttpResponse
from django.shortcuts import render


def demo(request):
    return render(request,"index.html")
def history(request):
    return render(request,"hise.html")
def Teachings(request):
    return render(request,"about.html")
def Images(request):
    return render(request,"ink.html")
def Contact(request):
    return render(request,"cont.html")
