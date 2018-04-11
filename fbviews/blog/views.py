from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel

def list_view(request):	
	template = "blog/index.html"
	query_set = PostModel.objects.all()
	print(query_set)
	context = {'query_set':query_set}
	return render(request, template, context)
