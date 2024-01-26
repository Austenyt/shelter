from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView

from dogs.forms import DogForm
from dogs.models import Category, Dog


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Питомник - Наши породы'
    }
    return render(request, 'dogs/categories.html', context)


def category_dogs(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Dog.objects.filter(category_id=pk),
        'category_pk': category_item.pk,
        'title': f'Собаки породы - все наши породы {category_item.name}'
    }
    return render(request, 'dogs/categories.html', context)


class DogCreateView(CreateView):
    model = Dog
    form_class = DogForm
