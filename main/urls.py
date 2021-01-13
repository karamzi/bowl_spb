from django.urls import path
from .views import index, ajax_parse_results, profile, calendar

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('calendar/', calendar, name='calendar'),
    path('api/parse_results/', ajax_parse_results),
]