from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вдалий вхід у кабінет користувача')
            return HttpResponseRedirect(reverse('simple_user:user_search'))
        else:
            messages.info(request, '<strong>Невдала спроба входу!</strong> Можливо, недійсний пароль. '
                                   'Перевірте, чи ввімкнений CapsLock.')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context=context)


def admin_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вдалий вхід у кабінет користувача')
            return HttpResponseRedirect(reverse('dashboard:dashboard'))
        else:
            messages.info(request, 'Невдала спроба входу. Можливо, недійсний пароль. Перевірте, чи вимкнений CapsLock.')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context=context)

