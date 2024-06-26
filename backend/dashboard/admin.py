from django.contrib import admin
from .models import MailItemModel, RecipientModel


class MailItemInline(admin.TabularInline):
    model = MailItemModel


# @admin.register(SenderModel)
# class SenderAdmin(admin.ModelAdmin):
#     list_display = ['sender_name']
#     list_display_links = ['sender_name']
#     change_list = ['street', 'build', 'build_letter', 'apartment']


@admin.register(RecipientModel)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ['street', 'build', 'build_letter', 'apartment']
    list_display_links = ['street']
    inlines = [MailItemInline]


# Register your models here.
@admin.register(MailItemModel)
class MailItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'track_number', 'address_id', 'is_court', 'is_court_subpoena',
                    'is_police_fine', 'date_of_receipt', 'expired_date']
    list_display_links = ['track_number']
    change_list = ['is_court', 'is_court_subpoena', 'is_police_fine']
    prepopulated_fields = {'slug': ('track_number', )}
