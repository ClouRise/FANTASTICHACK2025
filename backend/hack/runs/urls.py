from django.urls import path
from .views import RaceSimulationView, result_stat
from . import views
from .views import get_persons, PersonAPI, clear_results

urlpatterns = [
    path('api/race/', RaceSimulationView.as_view(), name='race-stream'),
    path('api/generate', views.result_stat, name='result_stat'), 
    path('api/persons/', PersonAPI.as_view(), name='persons_api'),
    path('api/persons/<int:person_id>/', PersonAPI.as_view(), name='person_detail_api'),
    path('api/clear/', clear_results, name='clear_results'),
 
]