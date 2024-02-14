from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import MailItemModel, RecipientModel
from .forms import AddLetterForm, SearchForm


# Create your views here.
def search_engine(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            wanted_letter = MailItemModel.objects.filter(
                Q(track_number__icontains=query) |
                Q(date_of_receipt__icontains=query)
            )

            context = {
                'query': query,
                'wanted_letter': wanted_letter,
            }

        return render(request, 'dashboard/search/search_results.html', context=context)


def index(request):
    return render(request, 'dashboard/index.html')


def letters_archive(request):
    letters = RecipientModel.objects.all()
    letters_paginator = Paginator(letters, 20)
    letters_number = request.GET.get('page')
    letters_numbers = letters_paginator.get_page(letters_number)

    context = {
        'letters': letters,
        'letters_numbers': letters_numbers,
    }

    return render(request, 'dashboard/letters_archive.html', context=context)


def add_letter(request):
    letters = MailItemModel.objects.all()[:1]

    if request.method == 'POST':
        form = AddLetterForm(request.POST)
        if form.is_valid():
            track_number = form.cleaned_data['track_number']
            if MailItemModel.objects.filter(track_number=track_number).exists():
                messages.warning(request, 'Такій лист вже був збережений раніше')
            else:
                MailItemModel.objects.create(**form.cleaned_data)
                return HttpResponseRedirect(reversed('dashboard:letters_archive'))
    else:
        form = AddLetterForm()

    context = {
        'form': form,
        'letters': letters,
    }

    return render(request, 'dashboard/add_letter.html', context=context)


def recipient_data(request, pk=None):
    recipient_address = RecipientModel.objects.get(pk=pk)
    recipient_data = RecipientModel.objects.filter(pk=pk)

    context = {
        'recipient_address': recipient_address,
        'recipient_data': recipient_data,
    }

    return render(request, 'dashboard/recipient_data.html', context=context)
