from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('about', views.about_me)
]