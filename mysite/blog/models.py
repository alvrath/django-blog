from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=200, default='', verbose_name='Заголовок')
    slug = models.SlugField(max_length=200)
      
    def __str__(self):
        return self.title

class Rubrika(models.Model):
    title = models.CharField(max_length=200, default='', verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, allow_unicode=True)
    
    def __str__(self):
        return self.title
        

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.ManyToManyField('Category', default='1', related_name='category')
    rubrika = models.ForeignKey('Rubrika', blank=True, default='rubrika', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title


