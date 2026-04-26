from django.contrib import admin
from .models import Movie, Director, Genre


# 🎬 MOVIE ADMIN
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director', 'is_active')
    filter_horizontal = ('genres',) 


# 🎥 DIRECTOR ADMIN
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'birth_date')


# 🏷️ NUEVO: GENRE ADMIN
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')