from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Post
def home(request):
    # context変数を使うと、postsリストを活用できる
    context ={
        "posts": Post.objects.all()
    }
    return render(request,'hello/home.html',context)

def about(request):
    return render(request,'hello/about.html')

def contact(request):
    return render(request,'hello/contact.html')

def base(request):
    return render(request,'hello/base.html')