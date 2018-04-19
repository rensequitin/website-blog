from django.shortcuts import render, redirect
from .models import PostModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import PostCreateForm


class IndexView(ListView):
	model = PostModel
	template_name = 'blog/index.html'


class PostDetail(DetailView):
	model = PostModel
	template_name = 'blog/detail.html'


class PostCreate(CreateView):
	# model = PostModel
	# fields = ['title','content']
	# success_url = reverse('blog:index')
	form_class = PostCreateForm
	template_name = 'blog/create.html'
	def get_success_url(self):
		return '{}'.format(reverse('blog:index'))

	def form_valid(self, form):
		form.instance.added_by = self.request.user 
		return super().form_valid(form)