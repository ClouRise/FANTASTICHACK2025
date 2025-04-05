from django.urls import path
from .views import RaceSimulationView, result_stat
from . import views
from .views import get_persons


urlpatterns = [
    path('api/race/', RaceSimulationView.as_view(), name='race-stream'),
    path('aaa/', views.result_stat, name='result_stat'), 
    path('api/persons/', get_persons, name='get-persons'),
 
]