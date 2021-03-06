"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login  # , logout
from django.urls import path
from django.conf.urls import include, url

from myblog.posts_feed import LatestEntriesFeed
from rest_framework import routers

from myblog import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include('myblog.urls')),
    url(r'^accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),

    path('login/', login, {'template_name': 'login.html'}, name="login"),
    path('logout/', login, {'next_page': '/'}, name="logout"),
    # url(r'^login/$', login, {'template_name': 'login.html'}, name="login"),
    # url(r'^logout/$', login, {'next_page': '/'}, name="logout"),
    path('latest/feed/', LatestEntriesFeed()),


    # rest
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))

]
