from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone


# Create your views here.
def polls_list(request):
    return render(request, 'admin/home.html', {})


def account(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'admin/account.html', {'posts': posts})