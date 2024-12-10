from django.urls import path
from .views import fizzbuzz

urlpatterns = [
    path('fizzbuzz/', fizzbuzz, name='fizzbuzz'),
]
