from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')
router.register('subject', views.SubjectViewSet, basename='subject')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
