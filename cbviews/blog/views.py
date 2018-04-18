from django.shortcuts import render
from .models import PostModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class IndexView(ListView):
	model = PostModel
	template_name = 'blog/index.html'

class PostDetail(DetailView):
	model = PostModel
	template_name = 'blog/detail.html'