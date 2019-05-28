from django.shortcuts import render, get_object_or_404
from .models import blog

def allblog(request):
    blogs = blog.objects
    return render(request, 'blogs/home.html', {'blogs':blogs})

def details(request,blog_id):
    detailblog = get_object_or_404(blog,pk=blog_id)
    return render(request, 'blogs/details.html', {'detailblog':detailblog})
