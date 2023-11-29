from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB' , 'Published'


    title=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    description=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    staus = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)




    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]



    def __str__(self):
            return self.title 

      


# Create your models here.
