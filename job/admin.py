from django.contrib import admin

# Register your models here.
from .models import Job , Category # import models

admin.site.register(Job) # push model job to admin panel
admin.site.register(Category)
