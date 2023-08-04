from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import CalculatePercentageViewSet

router = DefaultRouter()
router.register(r'calculate_percentage/', CalculatePercentageViewSet, basename='calculate_percentage')

urlpatterns = [
    path('', include(router.urls)),
    
]
