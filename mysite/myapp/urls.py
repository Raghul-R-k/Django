from django.urls import path # type: ignore
from .import views

urlpatterns = [
    path('Web1',views.Webpage1),
    path('Web2',views.Webpage2),
    path('Web3',views.Webpage3),
]
