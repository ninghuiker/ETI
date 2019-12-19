from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    #date_created
    #author
    
# Create your models here.
