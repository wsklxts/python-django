from django.db import models

# Create your models here.




class classes(models.Model):
    name = models.CharField(max_length=32)
    classesToTeacher=models.ManyToManyField("teacher")

class teacher(models.Model):
    name = models.CharField(max_length=32)

class student(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=32,default="0")
    csid = models.ForeignKey(classes,on_delete=models.CASCADE)
