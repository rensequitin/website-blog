from django.shortcuts import render
from django.http import HttpResponse

def home(request):	
	response = HttpResponse()
	print(dir(response))
	response.write("Hello")
	response.content = "Practice" # entire content
	response.status_code = 404 # console 404 not found
	return response