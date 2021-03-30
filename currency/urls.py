from django.urls import path
from .views import *

urlpatterns = [
    path('exchangeRate/', rate_exchange, name='response')
]