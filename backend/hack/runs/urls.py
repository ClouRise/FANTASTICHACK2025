from django.urls import path
from . import views

urlpatterns = [
    path('race_progress/', views.race_progress, name='race_progress'),
]