from django.db import models


# 🎬 DIRECTOR
class Director(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 🏷️ NUEVO: GENRE
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)  # IMPORTANTE: único
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='movies'
    )

    genres = models.ManyToManyField(
        Genre,
        related_name='movies',
        blank=True
    )

    # 🆕 NUEVO: POSTER DE PELÍCULA
    image = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)