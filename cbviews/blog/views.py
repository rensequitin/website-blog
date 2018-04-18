from django.shortcuts import render
from .models import PostModel
from django.views.generic.list import ListView


class IndexView(ListView):
	model = PostModel
	template_name = 'blog/index.html'