from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post, Category, Rubrika
from django.utils import timezone

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
	
def categories_list(request):
	category = Category.objects.all() # Получаем все категории
	return render(request, 'blog/categories_list.html', {'categories': category})
	
def rubriki(request):
	rubriki = Rubrika.objects.all() # Получаем все категории
	return render(request, 'blog/rubriki.html', {'rubriki': rubriki})

def category(request, slug):
	category = Category.objects.get(slug=slug) # Получаем категории из базы данных
	posts = Post.objects.filter(category=category) # Получаем записи блога и применяем сразу фильтрацию по категориям. Это означает, если зайти в категорию к примеру Django в которой есть на текущий момент 12 записей, то они все выведутся на странице
	return render(request, 'blog/category.html', {'posts': posts, 'category': category})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post})
