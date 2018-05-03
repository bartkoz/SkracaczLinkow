from django.db import models

# Create your models here.

def short():
    shortname=uuid4().hex
    return shortname

class Link(models.Model):
    link = models.URLField()
    short = models.CharField(max_length=10, blank=True)
