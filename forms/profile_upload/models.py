from django.db import models

class ProfileImage(models.Model):
    # userimage = models.FileField(upload_to='images')
    userimage = models.ImageField(upload_to='uploads/images')
    Name = models.CharField( max_length=50)

    
# Create your models here.
class ProfileImage1(models.Model):
    userimage = models.FileField(upload_to='images')
    Name = models.CharField( max_length=50)