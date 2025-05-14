from django.urls import path
from .views import *

urlpatterns = [
    path('', stats_view, name='statistics')
]