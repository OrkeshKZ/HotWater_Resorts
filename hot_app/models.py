from django.db import models

# Create your models here.

class HotSprings(models.Model):
    name = models.CharField(max_length=100)
    insta = models.TextField()
    
    def __str__(self):
        return self.name
    