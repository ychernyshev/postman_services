from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dashboard', dashboard, name='dashboard'),
    path('search', simple_search, name='search'),
    # path('results/', simple_search_results, name='results'),
    path('search_results/', search_engine, name='search_results'),
    path('archive/', mail_archive, name='mail_archive'),
    path('add_mail/', add_mail, name='add_mail'),
    path('mail_<str:slug>/update', MailUpdateView.as_view(), name='update_mail'),
    path('add_recipient', add_recipient, name='add_recipient'),
    path('recipient_data/<int:pk>/', recipient_data, name='recipient_data'),
    path('recipient_<int:pk>/edit', RecipientEditUpdateView.as_view(), name='recipient_edit')
]