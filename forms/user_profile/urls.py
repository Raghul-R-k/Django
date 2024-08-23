from django.urls import path
from .views import FormspageView,ThankYouView,formlistView
urlpatterns = [
    
    path('form/',FormspageView.as_view(),name = 'Form_page'),
    path('Thanks/',ThankYouView.as_view(),name = 'thankyou'),
    path('UserList/',formlistView.as_view(),name = 'forms')
]
