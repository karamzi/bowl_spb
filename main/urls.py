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
    path('documents/', main.documents, name='documents'),
    path('protocols/', main.protocols, name='protocols'),
    path('regulations/', main.regulations, name='regulations'),
    path('studentsTournaments/', main.students_tournaments, name='students_tournaments'),
]
