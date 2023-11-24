from django.shortcuts import render

from dogs.models import Category


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
