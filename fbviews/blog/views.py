from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import PostModel
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm
from django.urls import reverse

# @login_required or @login_required(login_url='/login/')
def list_view(request):	
	template = 'blog/index.html'
	query_set = PostModel.objects.all()	
	context = {'query_set':query_set,
			   'dict': {'name':'Mina'},
			   'num': 143,
			   'array_list':[123,143],
			   'boolean': True,
			  }
	return render(request, template, context)

def detail_view(request,pk):	
	# try:
	# 	obj = PostModel.objects.get(id=pk)
	# except:
	# 	raise Http404

	# query_set = PostModel.objects.filter(id=pk)
	# if not query_set.exists():
	# 	raise Http404
	# else:
	# 	obj = query_set.first()

	template = 'blog/detail.html'
	query_set = get_object_or_404(PostModel,pk=pk)
	context = {'query_set':query_set}
	return render(request, template, context)

@login_required
def delete_view(request,pk):	
	template = 'blog/delete.html'
	qs = get_object_or_404(PostModel,pk=pk)
	if request.method == "POST":
		qs.delete()
		return redirect(reverse('blog:list'))
	context = {'qs':qs}
	return render(request, template, context)

@login_required 
def create_view(request):	
	# if request.method == "POST"
	# 	form = PostModelForm(request.POST)
	# 	if form.is_valid():
	# 		form.save(commit=False)
	# 		print(form.cleaned_data)
	form = PostModelForm(request.POST or None)
	if form.is_valid():
		form.save(commit=False)
		form.save()
		print(form.cleaned_data)
		return redirect(reverse('blog:list'))
	template = 'blog/create.html'
	context = {'form':form}
	return render(request, template, context)

@login_required 
def update_view(request, pk=None):
	qs = get_object_or_404(PostModel,pk=pk)
	form = PostModelForm(request.POST or None, instance=qs)
	template = 'blog/update.html'
	context = {'form':form}
	if form.is_valid():
		form.save(commit=False)
		form.save()
		print(form.cleaned_data)
		return redirect(reverse('blog:detail',kwargs={'pk':pk}))	
	return render(request, template, context)

@login_required
def login_require_view(request):	
	print(request.user)	
	if not request.user.is_authenticated:
		raise Http404		

	print('Logged in')
	template = 'blog/index.html'
	query_set = PostModel.objects.all()
	print(query_set)
	context = {'query_set':query_set,
			   'dict': {'name':'Mina'},
			   'num': 143,
			   'array_list':[123,143],
			   'boolean': True,
			  }
	return render(request, template, context)
