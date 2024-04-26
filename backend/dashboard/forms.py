from datetime import datetime

from django import forms
from django.forms import TextInput

from .models import RecipientModel, MailItemModel


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control border-radius-top-start-0 border-radius-bottom-start-0',
        'placeholder': 'Пошуковий запит...', 'aria-label': 'search'
    }))


class SimpleSearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'p-3 form-control mr-sm-2 right-angle border-0 media-input',
        'placeholder': 'Пошуковий запит...', 'aria-label': 'search'
    }))


class AddMailDateField(forms.DateInput):
    input_type = 'date'


class AddMailForm(forms.Form):
    track_number = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control right-angle',
        'placeholder': 'Номер відстеження',
    }))
    address = forms.ModelChoiceField(label='', empty_label='отримувач',
                                     queryset=RecipientModel.objects.all(),
                                     widget=forms.Select(attrs={
                                         'class': 'form-control right-angle js-example-basic-single'
                                     }))
    date_of_receipt = forms.DateField(widget=AddMailDateField(attrs={'class': 'form-control right-angle media-input'}),
                                      initial=datetime.today())
    is_court = forms.BooleanField(label='Суд',
                                  initial=False,
                                  required=False,
                                  widget=forms.CheckboxInput(attrs={
                                      'class': 'form-check-input right-angle media-input'
                                  }))
    # the_expired_date = forms.DateField(widget=AddMailDateField(attrs={'class': 'form-control right-angle'}))
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


class UpdateMailModelForm(forms.ModelForm):
    track_number = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control right-angle',
        'placeholder': 'Номер відстеження',
    }))
    address = forms.ModelChoiceField(label='', empty_label='отримувач',
                                     queryset=RecipientModel.objects.all(),
                                     widget=forms.Select(attrs={
                                         'class': 'form-control right-angle js-example-basic-single'
                                     }))
    date_of_receipt = forms.DateField(widget=AddMailDateField(attrs={'class': 'form-control right-angle media-input'}),
                                      initial=datetime.today())
    is_court = forms.BooleanField(label='Суд',
                                  initial=False,
                                  required=False,
                                  widget=forms.CheckboxInput(attrs={
                                      'class': 'form-check-input right-angle media-input'
                                  }))
    # the_expired_date = forms.DateField(widget=AddMailDateField(attrs={'class': 'form-control right-angle'}))
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

    class Meta:
        model = MailItemModel
        exclude = [
            'slug', 'the_expired_date',
        ]


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
                                     required=False,
                                     widget=forms.Select(attrs={
                                         'class': 'form-control right-angle media-input media-input'}))
    apartment = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control right-angle media-input', 'placeholder': '№ квартири'
    }))
    company_name = forms.CharField(label='Назва фірми (опціонально)',
                                     required=False,
                                     widget=forms.TextInput(attrs={
                                         'class': 'form-control right-angle',
                                         'placeholder': 'Назва фірми (опціонально)'
                                     }))


class RecipientEditModelForm(forms.ModelForm):
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
                                     required=False,
                                     widget=forms.Select(attrs={
                                         'class': 'form-control right-angle media-input media-input'}))
    apartment = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control right-angle media-input', 'placeholder': '№ квартири'
    }))
    company_name = forms.ChoiceField(label='Назва фірми (опціонально)',
                                     required=False,
                                     widget=forms.TextInput(attrs={
                                         'class': 'form-control right-angle',
                                     }))

    class Meta:
        model = RecipientModel
        fields = [
            'street', 'build', 'build_letter', 'apartment', 'company_name'
        ]
        widgets = {
            'street': TextInput(attrs={'class': 'form-control right-angle'})
        }
