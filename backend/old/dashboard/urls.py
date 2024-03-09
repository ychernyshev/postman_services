from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashboard'),
    path('dashboard', index, name='dashboard'),
    path('search/', search_engine, name='search_results'),
    path('archive/', letters_archive, name='letters_archive'),
    path('add_letter/', add_letter, name='add_letter'),
    path('new_recipient', new_recipient, name='new_recipient'),
    path('recipient_data/<int:pk>/', recipient_data, name='recipient_data'),
]