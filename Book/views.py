from xmlrpc.client import ResponseError
from rest_framework import viewsets, permissions, generics, status
from rest_framework import Response
from rest_framework import APIView
from rest_framework import api_view

# Create your views here.

@api_view(['GET'])
def HelloAPI(request) :
    return Response("hello world!")