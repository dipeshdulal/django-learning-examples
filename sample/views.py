from django.http.response import Http404
from rest_framework import serializers
from rest_framework.response import Response
from sample import serializer
from sample.serializer import SnippetSerializer
from sample.models import Snippet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
# Create your views here.



class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
   

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, update or delete a snippet instance
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
