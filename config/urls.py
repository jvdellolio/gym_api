
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from config.api import views

urlpatterns = [
    path("exercise/", views.ExerciseList.as_view()),
    path("exercise/<int:pk>", views.ExerciseDetail.as_view()),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]

urlpatterns = format_suffix_patterns(urlpatterns)