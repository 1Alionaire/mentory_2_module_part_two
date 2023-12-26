from django.shortcuts import render, HttpResponseRedirect
from Posts.models import Post
from Posts.forms import InputBlogRecord
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

def main_page(request):
    context = {'title': 'Главная'}
    return render(request, 'index.html', context)

def all_posts(request):
    posts = Post.objects.all()
    context = {
        'title':'Все посты',
        'posts': posts
    }
    return render(request, context=context, template_name='all_posts.html')

def create_post(request):
    if request.method == "POST":
        form = InputBlogRecord(data=request.POST)
        if form.is_valid():
            need_data = form.save(commit=False)
            need_data.author = User.objects.get(username='admin')
            need_data.date_posted = datetime.now()
            form.save()
            return HttpResponseRedirect(reverse('Posts:all_posts'))
            # return HttpResponseRedirect(reverse('info(need_data.id)'))
    else:
        form = InputBlogRecord()
    context = {'title': 'Создать пост', 'form':form}
    return render(request, 'create_post.html', context)

def info_post(request, id):
    need_post = Post.objects.get(id=id)
    context = {
        'title': 'Подробно',
        'post': need_post
    }
    return render(request, 'info_post.html', context)
