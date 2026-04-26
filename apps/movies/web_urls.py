from django.urls import path
from .views import index, directors_page

urlpatterns = [
    path("index/", index),
    path("directors/", directors_page),
]