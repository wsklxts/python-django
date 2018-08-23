from django.db import models

# Create your models here.

#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
# class student(models.Model):
#     name = models.ForeignKey(Question, on_delete=models.CASCADE)
#     age = models.CharField(max_length=200)


class student2(models.Model):
    name = models.CharField(max_length=200)
    bbb = models.CharField(max_length=200,null=True)
    ccc = models.CharField(max_length=200,null=True)
    ddd = models.CharField(max_length=200,null=True)
    www = models.CharField(max_length=200)
    fff = models.CharField(max_length=200)
