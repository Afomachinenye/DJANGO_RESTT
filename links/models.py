from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class List(models.Model):
    target_url : models.URLField(max_length = 200)
    description : models.CharField(max_length = 200)  
    identifier: models.SlugField(max_length=20, unique=True, blank = True)  
    author :  models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date : models.DateTimeField (auto_now_add=True)
    active :  models.BooleanField(default=True) 