from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from sample.models import Snippet
from sample.serializer import SnippetSerializer

# Create your views here.

@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    List all the code snippets, or create a new code snippet
    """

    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    """
    Retreive, Update or delete a snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)

def say_hello(request):
    foo(name="dipesh", age=20, full_name="dipeshdulal")
    return render(request, 'hello.html', {'name': 'Dipesh'})

def foo(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])