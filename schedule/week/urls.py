from django.urls import path
from .import views

urlpatterns = [
    path('<int:days>', views.week),
    path('<str:days>', views.week_details,name='week-detail')
]