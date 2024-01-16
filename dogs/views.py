from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView

from dogs.models import Category, Dog


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Питомник - Наши породы'
#     }
#     return render(request, 'dogs/category_list.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Питомник - все наши породы'
    }


# def category_dogs(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Dog.objects.filter(category_id=pk),
#         'category_pk': category_item.pk,
#         'title': f'Собаки породы - все наши породы {category_item.name}'
#     }
#     return render(request, 'dogs/category_list.html', context)


class DogListView(ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Собаки породы - все наши породы {category_item.name}'

        return context_data


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'category',)
    successful_url = reverse_lazy('dogs:categories')


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'category',)

    def get_success_url(self):
        return reverse('dogs:category', args=[self.object.category.pk])


class DogDeleteView(UpdateView):
    model = Dog
    successful_url = reverse_lazy('dogs:categories')