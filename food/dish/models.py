from django.db import models

class dish(models.Model):
    dish_name=models.CharField(max_length=50)
    dish_price=models.IntegerField(max_length=5)
    cuisine=models.IntegerField(max_length=25)

