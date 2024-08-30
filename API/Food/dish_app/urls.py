from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewSet  # Import the DishViewSet instead of BookViewSet

# Create a router and register the DishViewSet with it
router = DefaultRouter()
router.register('', DishViewSet, basename='dish')  # Update basename to 'dish'

# Set the app name
app_name = 'dishapp'

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
