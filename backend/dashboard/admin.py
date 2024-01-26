from django.contrib import admin
from .models import LetterItemModel, RecipientModel


# @admin.register(SenderModel)
# class SenderAdmin(admin.ModelAdmin):
#     list_display = ['sender_name']
#     list_display_links = ['sender_name']
#     change_list = ['street', 'build', 'build_letter', 'apartment']


@admin.register(RecipientModel)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ['street', 'build', 'build_letter', 'apartment']
    list_display_links = ['street']


# Register your models here.
@admin.register(LetterItemModel)
class LetterItemAdmin(admin.ModelAdmin):
    list_display = ['track_number', 'is_court', 'is_court_subpoena',
                    'is_police_subpoena', 'date_of_receipt', 'expired_date']
    list_display_links = ['track_number']
    change_list = ['is_court', 'is_court_subpoena', 'is_police_subpoena']
    prepopulated_fields = {'slug': ('track_number', )}
