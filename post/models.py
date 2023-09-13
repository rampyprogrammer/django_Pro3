from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=1000)
    created_at=models.DateTimeField(default=datetime.now)
    body=models.TextField(max_length=1000000)

