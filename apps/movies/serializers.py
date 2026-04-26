from rest_framework import serializers
from .models import Movie, Director, Genre


# 🎥 DIRECTOR SERIALIZER
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


# 🏷️ NUEVO: GENRE SERIALIZER
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


# 🎬 MOVIE SERIALIZER
class MovieSerializer(serializers.ModelSerializer):

    director_detail = DirectorSerializer(source='director', read_only=True)

    # 🆕 mostrar géneros en lectura
    genres_detail = GenreSerializer(source='genres', many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'