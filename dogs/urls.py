from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import index, categories, category_dogs, DogCreateView

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/dogs/', category_dogs, name='category_dogs'),
    # path('dogs/create', DogCreateView.as_view(), name='dog_create'),
    # path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    # path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
    path('<int:pk>/dogs/create/', DogCreateView.as_view(), name='dog_create')
]
