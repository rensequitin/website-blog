from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.list_view, name='list'),    
    path('<int:pk>/', views.detail_view, name='detail'),
    path('<int:pk>/update/', views.update_view, name='update'),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
    path('create/', views.create_view, name='create'),
]