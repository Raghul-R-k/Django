from django.db import models

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=20)
    text = models.TextField()  # Changed to TextField to allow longer feedback
    rating = models.IntegerField()  # Removed max_length