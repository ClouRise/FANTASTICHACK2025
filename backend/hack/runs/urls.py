from django.urls import path
from .views import RaceSimulationView

urlpatterns = [
    path('api/race/', RaceSimulationView.as_view(), name='race-stream'),
]