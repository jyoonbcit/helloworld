# pages/urls.py
from django.urls import path, include
from .views import (homePageView, aboutPageView, jihoonPageView, results, homePost, todos, register, message,
                    logoutView, secretArea)

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('jihoon/', jihoonPageView, name='jihoon'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
    path('todos', todos, name='todos'),
    path("register/", register, name="register"),
    path('message/<str:msg>/<str:title>/', message, name="message"),
    path('', include("django.contrib.auth.urls")),
    path("logout/", logoutView, name="logout"),
    path("secret/", secretArea, name="secret")
]
