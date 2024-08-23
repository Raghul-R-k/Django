from django.shortcuts import render

from . models import Author

from .serializers import AuthorSerializer

from rest_framework.viewsets import ModelViewSet

 

# Create your views here.

class AuthorViewset(ModelViewSet):

    queryset = Author.objects.all()

    serializer_class = AuthorSerializer

