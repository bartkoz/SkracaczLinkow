from django.db import models
from uuid import uuid4

# Create your models here.

def short():
    shortname=uuid4().hex
    return shortname

class Link(models.Model):
    link = models.URLField()
    short = models.CharField(max_length=10, default=short)
    def __str__(self):
        return self.link
