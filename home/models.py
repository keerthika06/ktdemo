from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="profile")
