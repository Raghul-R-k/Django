from django.urls import path
from .views import land_page,second_page,detail_page

urlpatterns = [
    path('', land_page,name = 'land_page'),
    path('Card_detail/<int:card_id>', detail_page,name = 'detail_page'),
    path('cards', second_page,name = 'second_page'),
]