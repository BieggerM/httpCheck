from django.contrib import admin
from .models import Request
from .models import Session
# Register your models here.
admin.site.register(Request)
admin.site.register(Session)