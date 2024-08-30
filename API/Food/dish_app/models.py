from django.db import models
from category_app.models import Category  # Import the Category model


# Define a function to determine the upload path for dish images
def dish_image_path(instance, filename):
    return '/'.join([str(instance.name), filename])

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # Added to provide more details about the dish
    ingredients = models.TextField()  # Added to list ingredients used in the dish
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Added for price of the dish
    image = models.ImageField(upload_to=dish_image_path, null=True, blank=True)  # Optional image field
    category = models.ForeignKey(Category, related_name='dishes', on_delete=models.SET_NULL, null=True, blank=True)  # ForeignKey to Category

    
    def __str__(self):
        return self.name
