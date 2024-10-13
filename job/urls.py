from django.contrib import admin
from django.urls import path , include
from . import views


"""
Defines the app name for the 'job' app within the Django project.
"""
app_name = 'job'

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_detail,name='job_detail'),
    
]