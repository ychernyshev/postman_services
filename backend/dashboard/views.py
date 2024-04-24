from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import MailItemModel, RecipientModel
from .forms import AddMailForm, SearchForm, AddNewRecipientForm, RecipientEditModelForm, UpdateMailModelForm


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
                'title': 'Результати пошуку',
                'query': query,
                'wanted_letter': wanted_letter,
            }

        return render(request, 'dashboard/search_results.html', context=context)


@login_required(login_url='account:login')
def dashboard(request):
    context = {
        'title': 'Зведені дані',
    }

    return render(request, 'dashboard/dashboard.html', context=context)


@login_required(login_url='account:login')
def mail_archive(request):
    mails = MailItemModel.objects.all()
    mails_paginator = Paginator(mails, 20)
    mails_number = request.GET.get('page')
    mails_numbers = mails_paginator.get_page(mails_number)

    context = {
        'title': 'Архів листів',
        'mails': mails,
        'mails_numbers': mails_numbers,
    }

    return render(request, 'dashboard/mail_archive.html', context=context)


@login_required(login_url='account:login')
def add_mail(request):
    if request.method == 'POST':
        form = AddMailForm(request.POST)
        if form.is_valid():
            track_number = form.cleaned_data['track_number']
            if MailItemModel.objects.filter(track_number=track_number).exists():
                messages.info(request, 'Такій лист вже був збережений раніше')
            else:
                MailItemModel.objects.create(**form.cleaned_data)
                messages.success(request, 'Лист був збережений')
                return redirect('dashboard:add_mail')
    else:
        form = AddMailForm()

    context = {
        'title': 'Дадавання листа',
        'form': form,
        'letters': MailItemModel.objects.all()[:1],
    }

    return render(request, 'dashboard/add_mail.html', context=context)


class MailUpdateView(SuccessMessageMixin, UpdateView):
    model = MailItemModel
    form_class = UpdateMailModelForm
    template_name = 'dashboard/update_mail.html'
    # success_message = 'Дані листа оновлено'
    success_url = reverse_lazy('dashboard:mail_archive')


@login_required(login_url='account:login')
def add_recipient(request):
    if request.method == 'POST':
        form = AddNewRecipientForm(request.POST)
        if form.is_valid():
            street = form.cleaned_data['street']
            build = form.cleaned_data['build']
            build_letter = form.cleaned_data['build_letter']
            apartment = form.cleaned_data['apartment']

            validator_str = f'{street} {build}{build_letter}/{apartment}'
            sorted_str_from_model = []

            for item in RecipientModel.objects.filter(apartment=apartment):
                sorted_str_from_model.append(str(item))

            if validator_str in sorted_str_from_model:
                messages.info(request, 'Такий отримувач вже був доданий раніше')
            else:
                messages.success(request, 'Отримувач доданий')
                RecipientModel.objects.create(**form.cleaned_data)
    else:
        form = AddNewRecipientForm()

    context = {
        'title': 'Дадавання отримувача',
        'form': form,
    }

    return render(request, 'dashboard/add_recipient.html', context=context)


class RecipientEditUpdateView(SuccessMessageMixin, UpdateView):
    model = RecipientModel
    form_class = RecipientEditModelForm
    template_name = 'dashboard/update_recipient.html'
    success_message = 'Дані отримувача були оновлені'
    success_url = reverse_lazy('dashboard:mail_archive')


@login_required(login_url='account:login')
def recipient_data(request, pk=None):
    recipient_address = RecipientModel.objects.get(pk=pk)
    recipient_data = RecipientModel.objects.filter(pk=pk)
    recipient_data_paginator = Paginator(recipient_data, 5)
    recipient_data_number = request.GET.get('page')
    recipient_data_numbers = recipient_data_paginator.get_page(recipient_data_number)

    context = {
        'title': 'Дані отримувача',
        'recipient_address': recipient_address,
        'recipient_data': recipient_data,
        'recipient_data_numbers': recipient_data_numbers
    }

    return render(request, 'dashboard/recipient_data.html', context=context)
