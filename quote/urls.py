from django.urls import path
from quote.views import QuoteViewSet,user_quotes
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, basename='quotes')

#my url's and my additional route
urlpatterns = router.urls + [
    path('users/<int:id>/quotes/', user_quotes, name='user_quotes'),
]

