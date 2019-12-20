from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    author = models.CharField(max_length=30, null = True)
    
# Create your models here.
