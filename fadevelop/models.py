from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=300,unique=True)
    rank = models.PositiveIntegerField(unique=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name + " -- " + self.category.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=500, default="Post Title")
    review = models.TextField(max_length=1000, null=True, blank=True)   
    #the_body = RichTextField(blank=True, null=True)
    the_body = RichTextUploadingField(blank=True, null=True)
    release_datetime = models.DateTimeField(default=timezone.now) 
    image_cover = models.ImageField(null=True, blank=True, upload_to="images/", default="default.jpg")        
    url = models.SlugField(max_length=500 ,unique=True) #En {Ex: whats-is-django} 

    def __str__(self):
        return self.title
