from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def polls_list(request):
    return render(request, 'admin/home.html', {})


def account(request):
    return render(request, 'admin/account.html', {})