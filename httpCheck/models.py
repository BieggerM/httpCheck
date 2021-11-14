from django.db import models


# Create your models here.

class Request(models.Model):
    method = models.CharField(max_length=10)
    path = models.TextField()
    payload = models.TextField()
    scheme = models.CharField(max_length=10)
    session_id = models.TextField(default="null")


class Session(models.Model):
    session_id = models.TextField(null=False)
    session_start = models.TimeField(auto_now=True)
