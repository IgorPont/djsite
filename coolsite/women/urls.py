from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('cats/', categories) # http://127.0.0.1:8000/cats/
]