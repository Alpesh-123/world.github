from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')
router.register('course', views.CourseViewSet, basename='course')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
