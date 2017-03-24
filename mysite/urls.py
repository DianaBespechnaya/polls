from django.conf.urls import include, url
from django.contrib import admin

from polls import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'admin\login.html'
    }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('polls.urls')),
    ]