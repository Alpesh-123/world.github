
from django.contrib import admin
from django.urls import path,include
from api.views import CalculatePercentage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('percentage', CalculatePercentage.as_view()),
]
