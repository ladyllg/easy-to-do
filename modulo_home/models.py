from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class TodoItem(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.PROTECT)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    

class BackgroundFile(models.Model):
    img_path = models.ImageField(upload_to='background_img', blank=True)