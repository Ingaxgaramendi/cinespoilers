from django.shortcuts import render
from rest_framework import viewsets

from .models import Movie, Director, Genre
from .serializers import MovieSerializer, DirectorSerializer, GenreSerializer



# 🎬 MOVIES
def index(request):
    return render(request, "movies/index.html")


# 🎥 DIRECTORS
def directors_page(request):
    return render(request, "movies/directors.html")

# 🎬 MOVIES API
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# 🎥 DIRECTORS API
class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


# 🏷️ NUEVO: GENRE API
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer