from django.conf.urls import url
from django.contrib import admin

from recipes import views

urlpatterns = [
    url(r'^list/(?P<ingredients>.+?)/$', views.recipe_list, name='recipe_list'),
    url(r'^(?P<recipe_id>[0-9]+)/(?P<ingredients>.+?)/$', views.detail_view, name='detail'),
    url(r'^ingredients/', views.choose_ingredients, name='choose_ingredients'),
    url(r'^sms/$', views.sms),
]
