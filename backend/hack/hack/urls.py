from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('runs.urls', 'runs'), namespace='runs'))  #чутчут исправил, потом верну, если что
]
