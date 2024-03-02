from django import forms


class UserSearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'p-3 form-control mr-sm-2 right-angle outline media-input',
        'placeholder': 'Пошуковий запит...', 'aria-label': 'search'
    }))