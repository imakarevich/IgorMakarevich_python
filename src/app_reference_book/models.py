from django.db import models

# Create your models here.

class PublishingHouse(models.Model):
    name = models.CharField(max_length=40 )
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.pk} {self.name}'

class Authors(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40 )
    photo = models.ImageField(
        verbose_name="authors photo",
        upload_to='upload/%Y/%m/%d',
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.description}'

class Genres(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return f'{self.name} {self.description}'

class Series(models.Model):
    name = models.CharField(max_length=100 )
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.name} {self.description}'

