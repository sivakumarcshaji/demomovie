from django.db import models


# Create your models here.
class information(models.Model):
    name = models.CharField(max_length=250)
    house = models.CharField(max_length=250)
    age = models.IntegerField()
    qualification = models.TextField()

    def __str__(self):
        return self.name


class Movies(models.Model):
    name = models.CharField(max_length=250)
    star = models.CharField(max_length=250)
    img = models.ImageField()
    desc = models.TextField()

    def __str__(self):
        return self.name
