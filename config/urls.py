
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from config.api import views

urlpatterns = [
    path("exercise/", views.ExerciseList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)