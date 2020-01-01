from django.db import models
from datetime import datetime,time

# Create your models here.
class Todo_models(models.Model):
    content = models.TextField()
    date_todo = models.DateField(auto_now= False, auto_now_add=False, blank = True, null = True)

