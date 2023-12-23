from django.urls import path
from .views import *


urlpatterns =[
    path('', home, name='home-page'),
    path('history/', exchange_history, name='history')
]