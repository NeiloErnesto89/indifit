from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fitness-programs'),
    path('about/', views.about, name='fitness-about'),
]