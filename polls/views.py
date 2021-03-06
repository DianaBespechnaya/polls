from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate, login

#from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http import  HttpRequest
from django.template import RequestContext


def polls_list(request):
    return render(request, 'admin/home.html', {})


def sign_up(request):
    return render(request, 'admin/signup.html', {})

def my_login(request):
    context = RequestContext(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/profile/' + str(request.user) + '/')
            else:
                return redirect('/' + request.user + '/')
        else:
            return redirect('/' + request.user + '/')
    else :
        return render_to_response('admin/login.html', {}, context)


def account(request, user_name):
    me = request.user
    current_user = User.objects.get(username=user_name)
    posts = Post.objects.filter(author = current_user, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'admin/account.html', {'posts': posts , 'current_user':current_user})

def post_detail(request, pk, user_name):
    current_user = User.objects.get(username=user_name)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'admin/post.html', {'post': post , 'current_user':current_user})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, user_name=request.user)
    else:
        form = PostForm()
    return render(request, 'admin/post_edit.html', {'form': form})