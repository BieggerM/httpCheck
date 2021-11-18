from django.db import models
import random
import string


# Create your models here.

class Request(models.Model):
    method = models.CharField(max_length=10)
    path = models.TextField()
    payload = models.TextField()
    scheme = models.CharField(max_length=10)
    session_id = models.TextField(default="null")

    def get_method(self):
        return self.method


class Session(models.Model):
    session_id = models.TextField(null=False)
    session_start = models.TimeField(auto_now=True)

    def rand_str(self, chars=string.ascii_uppercase + string.digits, N=15):
        while True:
            random_string = ''.join(random.choice(chars) for _ in range(N))
            if not Session.objects.filter(session_id=random_string).exists():
                return ''.join(random.choice(chars) for _ in range(N))
