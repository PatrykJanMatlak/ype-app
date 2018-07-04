from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class ProductModel(models.Model):
    name        = models.CharField(max_length = 120, null = False, blank = False)
    price       = models.FloatField(null = True, blank = True)
    category    = models.CharField(max_length = 120,null = True, blank = True)
    mark        = models.FloatField(verbose_name="Your mark:",null = False, blank = False)
    evaluation  = models.TextField(verbose_name="Your opinion:",null = False, blank = False)
    created     = models.DateTimeField(auto_now=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null = True, blank = True)



    def __str__(self):
        return self.name

def product_slug_receiver (sender, instance, *args , **kwargs):
    correct_name = instance.name.replace(" ","-").lower()
    product_id = str(instance.id)
    if not instance.slug:
        instance.slug = correct_name + product_id
        instance.save()

post_save.connect(product_slug_receiver, sender = ProductModel)