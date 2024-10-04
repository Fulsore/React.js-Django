from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=225,unique=True)
    password = models.CharField(max_length=225)
    
    def __str__(self):
        return self.name
    
