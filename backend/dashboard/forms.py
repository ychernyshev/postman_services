from datetime import datetime

from django import forms

from .models import RecipientModel, LetterItemModel


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control mr-sm-2 right-angle outline media-input',
        'placeholder': 'Номер відстеження', 'aria-label': 'search'
    }))


class AddLetterDateField(forms.DateInput):
    input_type = 'date'


class AddLetterForm(forms.Form):
    track_number = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Номер відстеження',
    }))
    address = forms.ModelChoiceField(label='', empty_label='отримувач',
                                     queryset=RecipientModel.objects.all(),
                                     widget=forms.Select(attrs={
                                         'class': 'form-control'
                                     }))
    date_of_receipt = forms.DateField(widget=AddLetterDateField(attrs={
        'class': 'form-control right-angle media-input',
    }),
        initial=datetime.today())
    marks = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control'}))
    is_court = forms.BooleanField(label='Суд',
                                  initial=False,
                                  required=False,
                                  widget=forms.CheckboxInput(attrs={
                                      'class': 'form-check-input right-angle media-input'
                                  }))
    is_court_subpoena = forms.BooleanField(label='Повістка',
                                           initial=False, required=False,
                                           widget=forms.CheckboxInput(attrs={
                                               'class': 'form-check-input right-angle media-input'
                                           }))
    is_police_fine = forms.BooleanField(label='Поліцейський штраф',
                                        initial=False, required=False,
                                        widget=forms.CheckboxInput(attrs={
                                            'class': 'form-check-input right-angle media-input'
                                        }))
    letter_image_url = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Адреса фото',
    }))
    letter_image_id = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ID фото',
    }))
