from django.shortcuts import render
#from django.http import HttpResponse
from .models import Car

# Create your views here.
def home(request):
    cars=Car.objects.all()
    return render(request,'home.html',{'cars':cars})

def fun(request):
    car=Car.objects.all()#.get(id=id)
    return render(request,'main.html',{'car':car})
