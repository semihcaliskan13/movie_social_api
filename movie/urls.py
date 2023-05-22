from movie.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', UserViewSet, basename='movie')
urlpatterns = router.urls