from django.urls import path
from . import views

urlpatterns = [
     path('', views.Home, name="home"),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('deletetask/<int:task_id>/', views.deletetask, name='delete_task'),
     path('edittask/<int:task_id>/', views.edittask, name='edit_task'),
     path('setstatus/<int:task_id>/', views.set_status, name='set_status'),

]