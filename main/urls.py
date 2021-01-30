from django.urls import path
from . import views as main

app_name = 'main'

urlpatterns = [
    path('', main.index, name='index'),
    path('profile/<int:pk>/', main.profile, name='profile'),
    path('calendar/', main.calendar, name='calendar'),
    path('api/parse_results/', main.ajax_parse_results),
    path('goals/', main.goals, name='goals'),
    path('leadership/', main.leadership, name='leadership'),
]
