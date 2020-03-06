from django.urls import path
from . import views

urlpatterns = [
    # url() -> url estatica y dinamica - Django 1.x
    # path -> url estatica y re_path -> dinamica - Django 2.x >
    path('', views.index),
]