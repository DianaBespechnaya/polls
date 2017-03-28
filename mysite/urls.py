from django.conf.urls import include, url
from django.contrib import admin

from polls import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'admin\login.html'
    }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{
        'template_name': 'admin\home.html'
    }, name='logout'),
    url(r'^signup/', views.sign_up, name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('polls.urls')),
    ]