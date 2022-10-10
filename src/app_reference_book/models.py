from platform import mac_ver
from pydoc import describe
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class PublishingHouse(models.Model):
    # id - pk - autoincrement
    name = models.CharField(
        max_length=40 
    )
    description = models.TextField(
        blank=True,
        null=True
    )

class Authors(models.Model):
    first_name = models.CharField(
        max_length=40 
    )
    last_name = models.CharField(
        max_length=40 
    )
    description = models.TextField(
        blank=True,
        null=True
    )

class Genres(models.Model):
    name = models.CharField(
        max_length=50 
    )
    description = models.TextField(
        blank=True,
        null=True
    )

class Series(models.Model):
    name = models.CharField(
        max_length=100 
    )
    description = models.TextField(
        blank=True,
        null=True
    )

