import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular article")
    title = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    


    class State(models.IntegerChoices):
        FORSALE = 0, _('Creado')
        RESERVED = 1, _('Reservado')
        SOLD = 2, _('Vendido')
        
    state = models.IntegerField(choices=State.choices, default=State.FORSALE)
        
  
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('article-detail', args=[str(self.id)])

    
    

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name