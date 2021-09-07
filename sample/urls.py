from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>/", views.snippet_detail),
]