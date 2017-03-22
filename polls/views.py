from django.shortcuts import render

# Create your views here.
def polls_list(request):
    return render(request, 'admin/home.html', {})