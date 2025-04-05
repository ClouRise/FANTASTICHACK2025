from django.urls import path
from .views import RaceSimulationView, result_stat
from . import views

urlpatterns = [
    path('api/race/', RaceSimulationView.as_view(), name='race-stream'),
    path('aaa/', views.result_stat, name='result_stat'), 
]