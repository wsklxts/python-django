from django.db import models

# Create your models here.

from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    add_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name ="文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title