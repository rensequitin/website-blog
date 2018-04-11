from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.list_view, name='list'),    
    path('<pk>/', views.detail_view, name='detail'),
]