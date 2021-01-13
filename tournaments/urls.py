from django.urls import path
from .views import tournaments_list, current_tournament

app_name = 'tournaments'

urlpatterns = [
    path('tournaments/', tournaments_list, name='tournaments_list'),
    path('tournaments/<int:pk>/', current_tournament, name='current_tournament'),
]