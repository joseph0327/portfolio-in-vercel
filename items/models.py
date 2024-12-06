from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count
from ckeditor.fields import RichTextField

# Create your models here.
class Item(models.Model):
    item_name       = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = RichTextField(blank=True)  # Replaced TextField with RichTextField
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('item_detail', args=[self.category.slug, self.slug] )
    
    def __str__(self):
        return self.item_name


class Certificates(models.Model):
    cert_name       = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    images          = models.ImageField(upload_to='photos/products')
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('cert_detail', args=[self.category.slug, self.slug] )
    
    
    def __str__(self):
        return self.cert_name


class ItemGallery(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)
    
    def __str__(self):
        return self.item.item_name
    
    class Meta:
        verbose_name='itemgallery'
        verbose_name_plural='item gallery'
        

class ItemGalleryCerts(models.Model):
    cert = models.ForeignKey(Certificates, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)
    
    def __str__(self):
        return self.cert.cert_name
    
    class Meta:
        verbose_name='certgallery'
        verbose_name_plural='certificate gallery'