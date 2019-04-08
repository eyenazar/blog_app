from django.shortcuts import render
from .models import Post
posts = [
    {
        'author': 'Ainazar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Ainazar',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2019'
    }
]

def home(request):
    title = 'Home'
    context = {
        'posts': Post.objects.all(),
        'title': title
    }
    return render(request, 'blog/home.html', context)

def about(request):
    title = 'About'
    return render(request, 'blog/about.html', {'title': title})

