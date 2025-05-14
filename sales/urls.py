from django.urls import path
from .views import *

urlpatterns = [
    path('product/<int:product_id>', product_sales, name='product_sales'),
    path('course/<int:course_id>', course_sales, name='course_sales'),
    path('consultation/<int:consultation_id>', consultation_sales, name='consultation_sales'),
]