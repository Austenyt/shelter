from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import index, categories

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
]
