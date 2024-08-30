from django.shortcuts import render
from .models import Dish
from .serializer import DishSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status

class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get_serializer_class(self):
        # Optionally customize the serializer class based on the action
        return DishSerializer

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
                'message': 'An error occurred while fetching the dishes.',
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
                'message': 'Dish created successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while creating the dish.',
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
                'message': 'Dish updated successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while updating the dish.',
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
                'message': 'Dish partially updated successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while partially updating the dish.',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            })

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Dish deleted successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': 'An error occurred while deleting the dish.',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            })
