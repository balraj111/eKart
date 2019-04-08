from django.db import models
import os
import random

# Create your models here.

def get_file_name(filepath):
    base_name = os.path.basename(filepath)
    name,ext  = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3910209312)
    name,ext=get_file_name(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

class ProductManager(models.Manager):

    def all(self):
        return self.get_queryset().filter(active=True)

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        print(id,qs)
        if qs.count()==1:
            return qs.first()
        return None

class Product(models.Model):
    title       = models.CharField(max_length=250)
    slug        = models.SlugField(blank=True,unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    image       = models.ImageField(upload_to='products/',null=True,blank=True)
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)



    objects=ProductManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
