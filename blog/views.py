from django.shortcuts import render, get_object_or_404
from .models import Blog

# View that shows all blogs
def all_blogs(request):
    blogs=Blog.objects.all().order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

# View that shows the details of each blog post
def detail(request, blog_id):
    # If blog_id is not found, display 404 page
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})