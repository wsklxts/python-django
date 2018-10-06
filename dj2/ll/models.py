from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    pwd=models.CharField(max_length=64)
    type=models.ForeignKey("userType",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class userType(models.Model):
    name=models.CharField(max_length=32,verbose_name="用户类型")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '用户类型'

class Admin(models.Model):
    name=models.CharField(max_length=32)
    admin_to_user=models.ManyToManyField("user",related_name="ss")

    def __str__(self):
        return self.name
