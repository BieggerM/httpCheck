from django.db import models


# Create your models here.

class Request(models.Model):
    method = models.CharField(max_length=10)
    path = models.TextField()
    payload = models.TextField()
    scheme = models.CharField(max_length=10)
    sessionid = models.TextField(default="null")

