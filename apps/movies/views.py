from rest_framework import viewsets
from .models import Movie, Director
from .serializers import MovieSerializer, DirectorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer