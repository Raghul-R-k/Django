from rest_framework import serializers
from .models import Dish

class DishSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)  # For creating or updating dishes

    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'ingredients', 'price', 'image', 'category_id']
        read_only_fields = ['id', 'category_id']
