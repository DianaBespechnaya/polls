from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http import  HttpRequest


# Create your views here.
def polls_list(request):
    return render(request, 'admin/home.html', {})

def sign_up(request):
    return render(request, 'admin/signup.html', {})

def account(request):
    me = request.user
    posts = Post.objects.filter(author = me, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'admin/account.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'admin/post.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'admin/post_edit.html', {'form': form})