from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('examples', views.examples, name='examples'),
    ]