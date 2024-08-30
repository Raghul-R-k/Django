from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Category
from .serializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while fetching categories.',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            })

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                'status': status.HTTP_201_CREATED,
                'data': serializer.data,
                'message': 'Category created successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while creating the category.',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            })

    def update(self, request, *args, **kwargs):
        try:
            partial = False
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Category updated successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while updating the category.',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            })

    def partial_update(self, request, *args, **kwargs):
        try:
            partial = True
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Category partially updated successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while partially updating the category.',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            })

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Category deleted successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while deleting the category.',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            })
        


