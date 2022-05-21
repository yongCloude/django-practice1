from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializer_inherit import BookSerializer
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

@api_view(['GET'])
def HelloAPI(request) :
    return Response("hello world!")

@api_view(['GET', 'POST'])
def booksAPI(request) :
    if request.method == 'GET' : 
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST' :
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            
@api_view(['GET'])
def bookAPI(request, bid) :
    book = get_object_or_404(Book, bid = bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status.status.HTTP_200_OK)


class BooksAPI(APIView) :
    def get(self, request) :
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request) : 
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class BookAPI(APIView) :
    def get(self, request, bid) :
        book = get_object_or_404(Book, bid = bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status = status.HTTP_200_OK)



    