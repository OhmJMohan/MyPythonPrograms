from django.db import models

# Create your models here.

class Bookmark(models.Model):
    link = models.CharField(max_length=256)
    linkname = models.CharField(max_length=200)
    candidatemail = models.EmailField(max_length = 254)