from django.db import models


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/{0}.{1}".format(instance.id,extension)



# Create your models here.
class Job(models.Model): # table
    title = models.CharField(max_length=100) # field & column title
    # location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    discription = models.TextField(max_length=1000)
    puplished_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category",on_delete=models.CASCADE) # many to many relationship # when deleting the category the job will be deleted also
    image = models.ImageField(upload_to=image_upload)
    
    def __str__(self):
        return self.title
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    