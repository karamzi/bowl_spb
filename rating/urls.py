from django.urls import path
from .views import statistic, rating, upload_rating_ajax

app_name = 'rating'

urlpatterns = [
    path('statistic/', statistic, name='statistic'),
    path('rating/', rating, name='rating'),
    path('uploadRating/', upload_rating_ajax),
]