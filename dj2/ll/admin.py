from django.contrib import admin

# Register your models here.

from . import  models

admin.site.register(models.user)
admin.site.register(models.userType)
admin.site.register(models.Admin)
