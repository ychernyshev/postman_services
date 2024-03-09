from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import MailItemModel, RecipientModel
from .forms import AddMailForm, SearchForm, AddNewRecipientForm


# Create your views here.
@login_required(login_url='account:login')
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


@login_required(login_url='account:login')
def index(request):
    return render(request, 'dashboard/index.html')


@login_required(login_url='account:login')
def letters_archive(request):
    letters = RecipientModel.objects.all()
    letters_paginator = Paginator(letters, 20)
    letters_number = request.GET.get('page')
    letters_numbers = letters_paginator.get_page(letters_number)

    context = {
        'letters': letters,
        'letters_numbers': letters_numbers,
    }

    return render(request, 'dashboard/mails_archive.html', context=context)


@login_required(login_url='account:login')
def add_letter(request):
    letters = MailItemModel.objects.all().last()

    if request.method == 'POST':
        form = AddMailForm(request.POST)
        if form.is_valid():
            track_number = form.cleaned_data['track_number']
            if MailItemModel.objects.filter(track_number=track_number).exists():
                messages.warning(request, 'Такій лист вже був збережений раніше')
            else:
                MailItemModel.objects.create(**form.cleaned_data)
                return redirect('dashboard:add_letter')
    else:
        form = AddMailForm()

    context = {
        'form': form,
        'letters': letters,
    }

    return render(request, 'dashboard/add_mail.html', context=context)


@login_required(login_url='account:login')
def new_recipient(request):
    if request.method == 'POST':
        form = AddNewRecipientForm(request.POST)
        if form.is_valid():
            street = form.cleaned_data['street']
            build = form.cleaned_data['build']
            build_letter = form.cleaned_data['build_letter']
            apartment = form.cleaned_data['apartment']

            address_checking_list = [
                RecipientModel.objects.filter(street=street).exists(),
                RecipientModel.objects.filter(build=build).exists(),
                RecipientModel.objects.filter(build_letter=build_letter).exists(),
                RecipientModel.objects.filter(apartment=apartment).exists()
            ]
            if False in address_checking_list:
                messages.success(request, 'Отримувач доданий')
                RecipientModel.objects.create(**form.cleaned_data)
            else:
                messages.info(request, 'Отримувач вже був доданий раніше')
                print(f'recipient_address: {address_checking_list}')
    else:
        form = AddNewRecipientForm()

    context = {
        'form': form,
    }

    return render(request, 'dashboard/new_recipient.html', context=context)


@login_required(login_url='account:login')
def recipient_data(request, pk=None):
    recipient_address = RecipientModel.objects.get(pk=pk)
    recipient_data = RecipientModel.objects.filter(pk=pk)
    recipient_data_paginator = Paginator(recipient_data, 5)
    recipient_data_number = request.GET.get('page')
    recipient_data_numbers = recipient_data_paginator.get_page(recipient_data_number)

    context = {
        'recipient_address': recipient_address,
        'recipient_data': recipient_data,
        'recipient_data_numbers': recipient_data_numbers
    }

    return render(request, 'dashboard/recipient_data.html', context=context)
