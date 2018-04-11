from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel

def list_view(request):	
	template = "blog/index.html"
	query_set = PostModel.objects.all()
	print(query_set)
	context = {'query_set':query_set,
			   'dict': {'name':'Mina'},
			   'num': 143,
			   'array_list':[123,143],
			   'boolean': True,
			  }
	return render(request, template, context)
