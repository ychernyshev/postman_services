from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashboard'),
    path('dashboard', index, name='dashboard'),
    path('search/', search_engine, name='search_results'),
    path('archive/', mail_archive, name='mail_archive'),
    path('add_mail/', add_mail, name='add_letter'),
    path('mail_<str:slug>/update', MailUpdateView.as_view(), name='update_mail'),
    path('new_recipient', new_recipient, name='new_recipient'),
    path('recipient_data', recipient_data, name='recipient_data'),
    path('recipient_<int:pk>/edit', RecipientEditUpdateView.as_view(), name='recipient_edit')
]