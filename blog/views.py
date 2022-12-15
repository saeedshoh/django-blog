from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import * 

class HomeListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Classic Blog Design'
        return context

class PostCategoryView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(slug=self.kwargs['slug'])
        return context
    

    

def index(request):
    return render(request, 'blog/index.html')

def get_category(request, slug):
    return render(request, 'blog/category.html')

def get_post(request, slug):
    return render(request, 'blog/category.html')