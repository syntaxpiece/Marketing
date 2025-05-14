from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('informations/', informations, name='informations'),
]