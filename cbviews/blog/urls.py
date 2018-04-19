from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<slug>/detail/', views.PostDetail.as_view(), name="detail"),
    path('create/', views.PostCreate.as_view(), name="create"),
    path('<slug>/update/', views.PostUpdate.as_view(), name="update"),
    path('<slug>/delete/', views.PostDelete.as_view(), name="delete"),
]