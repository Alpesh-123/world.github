from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from api.views import StudentViewSet,CountryViewSet

router = DefaultRouter()
router.register(r'student', views.StudentViewSet, basename='student')
router.register(r'country', views.CountryViewSet, basename='country')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
