from django.urls import path
from .views import CreateProfileView,Profileview
urlpatterns = [
    
    path('',CreateProfileView.as_view()),
    path('renderingimage',Profileview.as_view()),

]
