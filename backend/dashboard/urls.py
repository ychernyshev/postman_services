from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashboard'),
    path('dashboard', index, name='dashboard'),
    path('archive/', letters_archive, name='letters_archive'),
    path('add_letter/', add_letter, name='add_letter'),
]