from datetime import datetime

from django import forms

from .models import RecipientModel, MailItemModel


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control mr-sm-2 right-angle outline media-input',
        'placeholder': 'Пошуковий запит...', 'aria-label': 'search'
    }))


class AddLetterDateField(forms.DateInput):
    input_type = 'date'


class AddMailForm(forms.Form):
    track_number = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control right-angle',
        'placeholder': 'Номер відстеження',
    }))
    address = forms.ModelChoiceField(label='', empty_label='отримувач',
                                     queryset=RecipientModel.objects.all(),
                                     widget=forms.Select(attrs={
                                         'class': 'form-control right-angle'
                                     }))
    date_of_receipt = forms.DateField(widget=AddLetterDateField(attrs={
        'class': 'form-control right-angle media-input',
    }),
        initial=datetime.today())
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
    letter_image_id = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control right-angle',
        'placeholder': 'ID фото',
    }))


class AddNewRecipientForm(forms.Form):
    street = forms.ChoiceField(label='Вулиця',
                               choices=RecipientModel.STREET,
                               widget=forms.Select(attrs={
                                   'class': 'form-control right-angle',
                               }))
    build = forms.ChoiceField(label='№ будинку (Літери немає по замовченню)',
                              choices=RecipientModel.BUILD,
                              widget=forms.Select(attrs={
                                  'class': 'form-control right-angle media-input media-input'}))
    build_letter = forms.ChoiceField(label='Літера будинку (Літери немає по замовченню)',
                                     choices=RecipientModel.BUILD_LETTER,
                                     widget=forms.Select(attrs={
                                         'class': 'form-control right-angle media-input media-input'}))
    apartment = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control right-angle media-input', 'placeholder': '№ квартири'
    }))
