from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here.

class ShopModel(models.Model):
    name        = models.CharField(max_length = 120)
    city        = models.CharField(max_length = 120, null=True, blank=True)
    street      = models.CharField(max_length = 120, null=True, blank=True)   
    open_at     = models.CharField(max_length = 5, null=True, blank=True, help_text="In HH:MM format.") 
    close_at    = models.CharField(max_length = 5, null=True, blank=True, help_text="In HH:MM format.") 
    created     = models.DateTimeField(auto_now_add=True) 
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return (self.name + " - " + self.city + ", " + self.street)
        except:
            return (self.name)

    def get_absolute_url(self):
        return reverse ("shops:details", kwargs = {"pk":self.pk})