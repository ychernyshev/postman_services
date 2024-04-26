from django.urls import path

from .views import *

urlpatterns = [
    path('search', user_search, name='user_search'),
]
