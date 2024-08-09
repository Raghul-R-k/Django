from django.urls import path
from .import views

urlpatterns = [
    path('<int:month>', views.monthly_details_by_number),
    path('<str:month>', views.monthly_details,name='month-detail')
]


#<PLace Holder>