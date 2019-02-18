from django.shortcuts import render
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^apply/$', views.how_to_apply, name='how_to_apply'),
    url(r'^privacy/$', views.privacy_policy, name='privacy_policy'),
    url(r'^faqs/$', views.faqs, name='faqs'),
]