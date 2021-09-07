from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    foo(name="dipesh", age=20, full_name="dipeshdulal")
    return render(request, 'hello.html', {'name': 'Dipesh'})

def foo(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])