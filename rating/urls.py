from django.urls import path
from .views import rating

app_name = 'rating'

urlpatterns = [
    path('rating/', rating, name='rating'),
]