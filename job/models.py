from django.db import models

# Create your models here.
class Job(models.Model): # table
    title = models.CharField(max_length=100) # field & column title
