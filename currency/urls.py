from django.urls import path
from .views import *

urlpatterns = [
    path('exchangeRate/', rate_exchange, name='exchangeRate'),
    path('exchangeRateComparison/', rate_exchange_comparison, name='exchangeRateComparison')
]
