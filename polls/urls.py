from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.polls_list, name='home'),
]