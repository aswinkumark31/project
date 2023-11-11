from django.contrib import admin
from . import models

# Register your models here.
class Product_display(admin.ModelAdmin):
    list_display=['title','description','completed','created_at']

admin.site.register(models.Task,Product_display)
