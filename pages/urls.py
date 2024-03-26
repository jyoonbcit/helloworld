# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, jihoonPageView, results, homePost, todos

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('jihoon/', jihoonPageView, name='jihoon'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
    path('todos', todos, name='todos')
]
