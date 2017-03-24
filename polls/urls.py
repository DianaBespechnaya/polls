from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', views.account, name='account'),
    url(r'^$', views.polls_list, name='home'),
]