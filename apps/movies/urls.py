from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, DirectorViewSet, GenreViewSet, index


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'directors', DirectorViewSet)

# 🆕 GENRE ROUTE
router.register(r'genres', GenreViewSet)


urlpatterns = router.urls