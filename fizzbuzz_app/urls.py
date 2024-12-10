from django.urls import path
from .views import fizzbuzz_view

urlpatterns = [
    path('api/fizzbuzz/', fizzbuzz_view, name='fizzbuzz'),
]
