"""coyote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns, settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from recipes import views as recipes_views
from recipes import urls as recipes_urls

from coyote import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', recipes_views.home_page, name='home'),
    url(r'^recipes/', include(recipes_urls)),
]

if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns()
