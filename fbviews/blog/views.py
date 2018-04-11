from django.shortcuts import render
from django.http import HttpResponse

def home(request):	
	print(request)
	print(dir(request)) # view available methods in request
	return HttpResponse("<h1>Hello</h1>")
