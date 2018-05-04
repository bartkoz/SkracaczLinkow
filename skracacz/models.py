from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.

def short():
    shortname=get_random_string(length=6)
    return shortname

class Link(models.Model):
    link = models.URLField()
    short = models.CharField(max_length=10, default=short)
    def __str__(self):
        return self.link
