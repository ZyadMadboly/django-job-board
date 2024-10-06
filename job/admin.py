from django.contrib import admin

# Register your models here.
from .models import Job # import model job

admin.site.register(Job) # push model job to admin panel
