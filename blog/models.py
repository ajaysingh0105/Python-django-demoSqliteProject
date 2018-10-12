from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import os, shutil
from .choices import * 

def blog_directory_path(instance, filename):
    #return 'blogs/{0}/{1}'.format(instance.pk,'featured/'+filename)
    return 'blogs/{0}/{1}'.format('featured/',filename)
    
        
#def updateImage(self, instance):
    #path = instance.featured_image
    #newPath = path.replace('None', str(instance.pk))
    #shutil.move(path, newPath)

class Category(models.Model):
    title = models.CharField(unique=True, max_length=300)
    text = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    status = models.IntegerField(choices=RELEVANCE_CHOICES, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        instance.slug = slugify(instance.title)
        instance = self.save()
        
    def __str__(self):
        return self.title
        

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(unique=True, max_length=300)
    text = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True, )
    status = models.IntegerField(choices=RELEVANCE_CHOICES, default=0)
    #featured_image = models.ImageField(upload_to='media/temp', blank=True, null=True, default='default.jpg')
    featured_image = models.ImageField(upload_to=blog_directory_path, blank=True, null=True, default='default.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        instance.slug = slugify(instance.title)
        self.save()
        #updateImage(self, instance)
        
    def __str__(self):
        return self.title
       