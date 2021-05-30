from django.urls import path
from . import views
from task.views import home

urlpatterns = [
    path('', views.home , name='home') ,
    path('task/', views.home , name='home') ,
    path('add/', views.home , name='home') ,
    path("delete/<int:task_id>/", views.delete_view , name='delete_view')
]