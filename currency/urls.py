from django.urls import path
from .views import *

urlpatterns = [
    path('', response, name='response')
]