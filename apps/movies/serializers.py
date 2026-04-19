from rest_framework import serializers
from .models import Movie, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director_detail = DirectorSerializer(source='director', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'