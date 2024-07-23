from django.contrib import admin
from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('incomplete/<int:pk>/', views.task_incomplete, name='task_incomplete'),
]