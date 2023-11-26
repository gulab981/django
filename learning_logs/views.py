from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base(request):
	return render(request,'base.html')
	
def navbar(request):
	return render(request,'navbar.html')
	
def mobile(request):
	return render(request,'mobile.html')

def desktop(request):
	return render(request,'desktop.html')
