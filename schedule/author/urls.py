from django.urls import path # type: ignore
from .views import author_list, author_detail

urlpatterns = [
    path('author/', author_list, name='author_list'),
   
    # path('author/<slug:slug>/',author_detail, name='author_detail'),
    path('authors/<int:author_id>/',author_detail, name='author_detail'),
]
