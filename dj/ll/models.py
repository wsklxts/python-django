from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=32,default="0")

class classes(models.Model):
    name = models.CharField(max_length=32)

class teacher(models.Model):
    name = models.CharField(max_length=32)


