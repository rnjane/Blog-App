from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('create-category', views.CategoriesCreateView.as_view(), name='create_category'),
]