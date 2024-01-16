from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import index, CategoryListView, DogListView, DogCreateView

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/dogs/', DogListView.as_view(), name='category'),
    path('dogs/create', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update', DogUpdateView.as_view(), name='dog_update'),
]
