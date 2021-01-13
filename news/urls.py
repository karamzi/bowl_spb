from django.urls import path
from .views import news_list, current_news

app_name = 'news'

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', current_news, name='current_news'),
]
