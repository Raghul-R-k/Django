from django.shortcuts import render
from . models import Book
from .serializer import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
 

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get_serializer_class(self):
                if self.action == 'list':
                    return BookSerializer
                return self.serializer_class
        
   
    def list(self,request):
            try:
                book_objs = Book.objects.all()
                serializer = self.get_serializer(book_objs,many=True)
                return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data
                })
    
            except Exception as e:
                print(e)
                raise APIException({
                    'message':APIException.default_detail,
                    'status':APIException.status_code
                })

    def create(self,request):
            try:
                serializer = self.get_serializer(data=request.data)
                if not serializer.is_valid():
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'data':serializer.errors,
                        'message':'Inavlid Data'
                    })
                serializer.save()
                return Response({
                'status': status.HTTP_201_CREATED,
                'data': serializer.data,
                'message': 'Author created successfully'
            })
            except Exception as e:
                print(e)
                raise APIException({
                    'message':APIException.default_detail,
                    'status':APIException.status_code
                })
    #update all fields of book
    def update(self,request,pk=None):
        try:
            book_objs = self.get_object()
            serializer = self.get_serializer(book_objs,data=request.data,partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'book Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
    #update specifie
    def partial_update(self,request,pk=None):
        try:
            book_objs = self.get_object()
            serializer = self.get_serializer(book_objs,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'book Partial Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
 
    def destroy(self,request,pk=None):
        try:
            
            book_objs = self.get_object()
            book_objs.delete()
 
            return Response({
                'status': status.HTTP_200_OK,
                'message':'book deleted successfully'
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })