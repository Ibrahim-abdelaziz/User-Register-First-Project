from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class staff(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    age = models.IntegerField()
    birthday = models.DateField()
    img = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class info(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    jobs=models.CharField(max_length=50)
    lang=models.CharField(max_length=50)
    num=models.IntegerField()
