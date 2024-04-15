from django.urls import path

from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('', MovieTemplate, name='index'),
    path('movie/list', MovieList, name='list'),
    path('movie/<int:pk>', MovieDetail, name='detail'),
]